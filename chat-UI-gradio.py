import os
# pip install gradio
import gradio as gr
# pip install openai
import openai
# pip install python-dotenv (assuming you place key in an env)
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# the commented-out message_history variable is an example of when you want to establish some ground rules with what your API can and can't do. To keep it open ended like a normal chat, then just make an empty list.
# message_history = [{"role": "user", "content": f"You are a joke bot. I will specify the subject matter in my messages, and you will reply with a joke that includes the subjects I mention in my messages. Reply only with jokes to further input. If you understand, say OK."},
#                    {"role": "assistant", "content": f"OK"}]
message_history = []

def predict(input):
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=message_history
    )
    reply_content = completion.choices[0].message.content
    
    message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    
    # This version of the response variable works when dealing with a more established starting message_history
    # response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0, len(message_history)-1, 2)]
    
    return response

with gr.Blocks() as demo: 
    chatbot = gr.Chatbot() 

    with gr.Row(): 
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    txt.submit(predict, txt, chatbot)

    txt.submit(None, None, txt, _js="() => {''}")

demo.launch()