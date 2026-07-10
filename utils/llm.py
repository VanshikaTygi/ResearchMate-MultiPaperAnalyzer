from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, context):

    prompt = f"""
    You are ResearchMate AI, an expert research assistant.

    Answer the question using only the provided research context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )


    return response.choices[0].message.content