import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

Client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))


def make_research(query):
    url = "https://www.google.com/search"
    data = requests.get(url, params={'q': query})

    soup = BeautifulSoup(data.text, 'html.parser')

    raw_data = soup.body.find(attrs={"id": "main"}).get_text().strip()

    messages = [
        {
            "role": "system",
            "content": "Prepare for me a well formatted document [should not have markdown in the data] as a research an a potential lead i will be having meeting with this should as complete as possible use the google search content provide below to get all information about the client include any link and profile of the person and connections of the client with other entities, job history, location and many more in preparation of our meeting"
        },
        {
            "role": "assistant",
            "content": "Please provide me the google search data of the client"
        },
        {
            "role": "user",
            "content": f"```{raw_data}```"
        }
    ]
    response = Client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=.5)

    return response.choices[0].message.content
