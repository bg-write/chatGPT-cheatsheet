'''A chatbot using the Gradio UI library.'''
import os
import gradio as gr
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{
    "role":
    "system",
    "content":
    "You are a music curator with decades of experience in the music industry who helps people discover great new music from any era or genre. You value the classics yet always try to steer new listeners to discover music they might not have heard before."
}]


def custom_chat(user_input):
    '''Prompts user input, sends to OpenAI, prints response'''
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=10,
    )
    chat_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_reply})
    return chat_reply


demo = gr.Interface(fn=custom_chat,
                    inputs="text",
                    outputs="text",
                    title="Discover Your New Favorite Songs!")

demo.launch(share=True)
