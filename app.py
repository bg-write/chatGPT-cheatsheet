import os
import openai # pip install openai
from dotenv import load_dotenv # pip install python-dotenv (assuming you place your API key in an env file)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
  '''A function that prompts the user for an input, sends that input to OpenAI for processing, and then prints a response'''
  message_history = []
  while True:
    user_input = input("USER PROMPT > ")
    print("USER INPUT:", user_input, "...")

    message_history.append({"role":"user", "content":user_input})

    try:
      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # can use "gpt-3.5-turbo" (cheaper) or "text-davinci-003" (pre-trained yet more expensive)
        messages=message_history,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
      )
      reply_content = completion.choices[0].message.content
      print("CHATGPT RESPONSE:", reply_content)
    except openai.error.OpenAIError as error:
      print("OpenAI API error:", error)
    except Exception as error:
      print("Unknown error occurred:", error)

if __name__ == '__main__':
  chatbot()

# > python app.py