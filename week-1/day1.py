import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

"""
message = "Hello, GPT! This is my first message to you! Hi!"
messages = [{"role": "user", "content": message}]
openai = OpenAI()
response = openai.chat.completions.create(model="gpt-5-nano", messages=messages)
print(response.choices[0].message.content)
"""

ed = fetch_website_contents("https://edwarddonner.com")
# print(ed)

system_prompt = """
You are an assisstant, that analyzes the content of the website,
and provide a short summary, ignoring the text that might be navigation related.
Respond in markdown
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""

#messages = [{"role": "system", "content": "you are a snarky assisstant sounds like a pirate"},
#            {"role": "user", "content": "what is 2 + 2 ?"}]

openai = OpenAI()

def messages_for(website):
    return [
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": user_prompt_prefix + website }
    ]


def summarize(url):
    website = fetch_website_contents(url)
    response = openai.chat.completions.create(model="gpt-4.1-nano", messages=messages_for(website))
    return response.choices[0].message.content

def display_summary(url):
    res = summarize(url)
    print(res)

res = display_summary("https://edwarddonner.com")
print(res)