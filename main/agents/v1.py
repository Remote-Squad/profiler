import os

import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

Client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))


def make_research(query):
    url = "https://www.google.com/search"
    data = requests.get(url, params={'q': query})

    soup = BeautifulSoup(data.text, 'html.parser')

    text_data = soup.body.find(attrs={"id": "main"}).get_text().strip()

    x, y = text_data.find("Verbatim") + 8, text_data.find("Next >")

    text_data = text_data[x:y]

    messages = [
        {
            "role": "user",
            "content": f"""
Carry out a comprehensive background search on the query {query}, i have included below copied text from the google search result for the query. include only information which is directly related to the query and try as much not to miss any facts the desired output is described below.

desired output must include Key roles and duration at Remote Squad, Major contributions and technical skills, Public Recognition and Activities, Highlights from online platforms, Personal Background, professional background and areas of specialization and any other important data based on copied text

google search data:
```{text_data}```
"""
        },
    ]


    response = Client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=.5)

    return response.choices[0].message.content
