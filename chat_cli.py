'''A chatbot that works in your command line interface.'''
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def chatbot():
    '''Prompts user input, sends to OpenAI, prints response'''
    message_history = []

    while True:
        user_input = input("USER PROMPT > ")
        print(f"YOU ASKED: '{user_input}' ...")

        message_history.append({"role": "user", "content": user_input})

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message_history,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            reply_content = completion.choices[0].message.content
            print("CHATGPT RESPONSE:", reply_content)

            message_history.append({
                "role": "assistant",
                "content": reply_content
            })

        except openai.error.OpenAIError as error:
            print("OpenAI API error:", error)


if __name__ == '__main__':
    chatbot()
