import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hey, Groq, how you doing? What Word will I learn today?"
        },
        {
            "role": "system",
            "content": 
                """Forneça frases simples no idioma em inglês. 
                Quando explicar um termo em inglês, explique-o em português.
                Forneça exemplos em inglês e sua tradução para o português .
                Em todo final de texto, solicite que o usuário tente utilizar 
                a palavra em uma frase simples."""
        }
    ],
    model="llama3-70b-8192"
)

print(chat_completion.choices[0].message.content)
