#### Referring to tutorial at: https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

import os
import json
import openai

# read json file
with open("path.json") as f:
    path = json.load(f)
openai.api_key = path["key"]

modes = [
    "one_question",
    "conversation",
]
mode_n = 1

# If only as one question
if modes[mode_n] == "one_question":
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Tell the world about the ChatGPT API in the style of a pirate.",
            }
        ],
    )

    print(completion.choices[0].message.content)

# If having a conversation with ChatGPT
elif modes[mode_n] == "conversation":
    messages = [{"role": "system", "content": "You’re a kind helpful assistant"}]

    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    chat_response = completion.choices[0].message.content
    print(f"ChatGPT: {chat_response} \n")

    messages.append({"role": "assistant", "content": chat_response})

    while True:
        content = input("User: ")
        messages.append({"role": "user", "content": content})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        chat_response = completion.choices[0].message.content
        print(f"ChatGPT: {chat_response} \n")
        messages.append({"role": "assistant", "content": chat_response})
