from urllib.parse import quote, urlparse, parse_qs
from urllib.request import urlopen

import html2text
import markdown
from bs4 import BeautifulSoup
import openai

import os
from dotenv import load_dotenv

load_dotenv()

client = openai.Client(api_key=os.getenv('OPENAI_API_KEY'))


def markdown_to_string(markdown_text) -> str:
    html = markdown.markdown(markdown_text)

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = True
    plain_text = h.handle(html)

    # Remove any remaining Markdown artifacts
    plain_text = plain_text.replace('*', '').replace('#', '').strip()

    return plain_text


def summarize(data: list[dict], query) -> str:
    obj = []
    for i in data:
        del i['displayed_url']
        obj.append(i)


    messages = [
        {
            "role": "system",
            "content": f"""Synthesize a concise summary from the provided data set, adhering to these specifications:

1. Data source: Google search results for the query "{query}"
2. Content: Include only factual information directly relevant to the query
4. Links: all links given have to be in the data given under the ['url'] key i.e no ai formulating non existing links
3. Format:
   - Use markdown for structure
   - Employ headers (H2, H3) to organize main topics and subtopics
   - Utilize bullet points for listing key details
4. Citations: Include hyperlinks to original sources for each main point
5. Length: 250-350 words
6. Style: Formal and objective, suitable for professional meeting preparation
7. Structure:
   - Introduction (1-2 sentences stating the query and summary purpose)
   - Main body (3-5 key topics, each with 2-3 supporting points)
   - Conclusion (1-2 sentences summarizing key takeaways)

Output the summary content only, without additional commentary or metadata."""
        },
        {
            "role": "assistant",
            "content": "Please provide me the row data. as you said i only will return the summary to help in the meeting preparation"
        },
        {
            "role": "user",
            "content": obj.__str__(),
        }
    ]


    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=.2)

    return response.choices[0].message.content


def parse_html_blocks(html_content) -> list[dict]:
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all top-level div elements that contain the result blocks
    result_blocks = soup.find_all('div')

    # print(result_blocks)

    parsed_results = []

    for block in result_blocks:
        result = {}

        # Extract the title and URL
        a_tag = block.find('a')
        if a_tag:
            title_div = a_tag.find('div', recursive=False)
            if title_div:
                result['title'] = title_div.get_text(strip=True)

            href = a_tag.get('href', '')
            if href.startswith('/url?'):
                parsed_url = urlparse(href)
                query_params = parse_qs(parsed_url.query)
                if 'q' in query_params:
                    result['url'] = query_params['q'][0]

        # Extract the description
        desc_div = block.find('div', class_=lambda x: x and 'BNeawe' in x and 's3v9rd' in x)
        if not desc_div:
            continue

        result['description'] = desc_div.get_text(strip=True)

        # Extract the displayed URL
        display_url_div = block.find('div', class_=lambda x: x and 'BNeawe' in x and 'UPmit' in x)
        if display_url_div:
            result['displayed_url'] = display_url_div.get_text(strip=True)

        try:
            if result["description"] and result["title"] and result["url"]:
                pass

        except KeyError as e:
            continue

        if result in parsed_results:
            continue

        if result:  # Only append if we found some content
            try:
                tester = result["displayed_url"]
                if not result["description"] == "View on Twitter":
                    parsed_results.append(result)
            except KeyError:
                pass

    return parsed_results


def make_research(query: str) -> str:
    url = "https://www.google.com/search?query=" + quote(query)

    with urlopen(url) as response:
        parsed_data = parse_html_blocks(response.read())

        print(parsed_data)

        summary = summarize(parsed_data, query)

        return markdown_to_string(summary)

