import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generate_summary(news_body: str) -> str:
    client = Groq()
    chat_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in news summarization in Bengali. Please summarize the following news article in 3-5 bullet points in Bengali."
            },
            {
                "role": "user",
                "content": news_body
            }
        ],
        temperature=0,
        max_tokens=32768,
        top_p=1,
        stream=False,
        stop=None,
    )
    return chat_completion.choices[0].message.content
