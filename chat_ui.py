'''A chatbot using the Gradio's UI.'''
import os
# pip install gradio
import gradio as gr
# pip install openai
import openai
# pip install python-dotenv (assuming you place key in an env)
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{
    "role":
    "system",
    "content":
    "You are a music curator who helps people discover great new music from any era or genre."
}]


def custom_chat(user_input):
    '''Prompts user input, sends to OpenAI, prints response'''
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages)
    chat_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chat_reply})
    return chat_reply


demo = gr.Interface(fn=custom_chat,
                    inputs="text",
                    outputs="text",
                    title="Discover Your New Favorite Songs!")

demo.launch(share=True)
