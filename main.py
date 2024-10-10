import os
from together import Together
from api import apikey #Insert your API Key from Together AI

client = Together(api_key=apikey)
def chat(prompt):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        messages=[
            {
                    "role": "user",
                    "content": f"{prompt}"
            }
    ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"],
        stream=False
    )
    print(f"AI:{response.choices[0].message.content}")

while True:
    show= input("User:")
    if show == 0:
        break
    else:
        chat(show)
        