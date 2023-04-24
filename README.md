<a name="top"></a>

# ChatGPT Cheatsheet

A guide to how ChatGPT can help us (written by a skeptic).

> V1: Completed April 24, 2023.
>
> V2: WIP (adding more specific API documentation).

[![GitHub issues](https://img.shields.io/github/issues/bg-write/chatGPT-cheatsheet?style=flat-square)](https://github.com/bg-write/chatGPT-cheatsheet/issues)

![image](https://doodleipsum.com/700x700?bg=D96363&i=7bba2d304a189734c2a8226c512748dd)

## The TL;DR

- _ChatGPT, and AI in general, is less like C-3PO and more like a bunch of well-meaning worms doing their best._
- _You don't have to know code to use ChatGPT; all you need to get started is a free [OpenAI](https://openai.com/blog/chatgpt) account._
- _If you're a developer trying to study ChatGPT's API and make your first chatbot, please also refer to the `chat_cli.py` and `chat_ui.py` files found in this repo._
- _AI is only as good as the data it's trained on. The better and more specific your prompt, the better ChatGPT can work for you._
- _Check out the [API Reference](#api-reference) section to see various examples of what you can (and can't) (and shouldn't) do with ChatGPT and its API._
- _This guide is like a menu: pick and choose whatever you need._

---

## Table of Contents

I. [Introduction](#intro)

- Overview of ChatGPT
- Metaphors For What ChatGPT Can (and Can't) Do
- Project Goals and Intended Audience

II. [Getting Started](#getting-started)

- System Requirements
- Installing Dependencies
- Running the Code

III. [Usage](#usage)

- Overview of Features
- Using `chat_cli.py` (ChatGPT in the Command Line)
- Using `chat_ui.py` (ChatGPT Deployed on Localhost)

IV. [Examples of ChatGPT Prompts and Best Practices](#prompt-examples)

- General Learning, Troubleshooting, Or Brainstorming
- Creating Your Own Study Guide
- Generating Project Ideas
- Preparing Your Resume For A Specific Application
- Preparing For A Job Interview
- Working In Excel
- Writing Shell (Linux) Commands
- Writing Git Commands
- Improving Code & Getting Feedback
- Extracting Data
- Generating Dummy Data
- Generating Documentation
- Understanding and Fixing Errors
- Writing Tests
- Building An API
- Natural Language Programming
- Python Examples
- HTML, CSS, and JavaScript Examples
- React Examples
- SQL Examples

V. [API Reference](#api-reference)

- Overview of the OpenAI API
- Obtaining an API key
- Examples of API usage

VI. [Giving Thanks](#legal)

- Closing Credits
- Cited Sources

VII. [Glossary](#glossary)

- Artificial Intelligence (AI)
- Machine Learning
- Natural Language Processing (NLP)
- Chatbot
- Deep Learning
- Neural Network
- Generative Model
- Transformer Model
- API (Application Programming Interface)

![image](https://doodleipsum.com/700x700?bg=D96363&i=0ca4af8cbb660d47f4f18a56fe91ab5b)

## I. Introduction <a name="intro"></a>

[Return to top](#top)

### Overview of ChatGPT

ChatGPT is a computer program that can understand and generate human-like language to have conversations with people.

> _This is the answer I got when I asked ChatGPT to explain itself in one sentence to someone who knows nothing about ChatGPT or AI._

Here's a more specific definition:

ChatGPT is a state-of-the-art, large-scale natural language processing model based on the Transformer architecture, which can generate human-like text and perform various language-related tasks with high accuracy.

> _This time, I asked ChatGPT to sum itself up in one sentence to an AI and machine learning expert. Pretty cool, right?_

OK ... but what does this all mean?

**AI (Artificial Intelligence)** is a type of computer technology that allows machines to perform tasks that normally require human intelligence. **Machine Learning** is a subset of AI that enables machines to learn from data and improve their performance without being explicitly programmed; in a way, it's learning from itself. Give it a goal and a data set to learn from and it'll do the rest.

So in relation to AI and machine learning, **ChatGPT** is a particular machine learning model that has been trained on a _lot_ of text data to generate human-like responses and carry out natural language processing tasks.

**Natural language processing models** are AI models that enable computers to understand, interpret, and generate human language, allowing them to interact with humans through speech or text. There are many types of AI models (which I'll detail in a future version of this guide). For now, it's important to know that ChatGPT uses the **Transformer** model. Compared to other AI models, the Transformer model is better at generating responses that focus on the _context_ of a conversation. What makes ChatGPT special is that it can be picky and focus on the most relevant parts of a user's input instead of having to process an entire sequence at once.

> _If you'd like to read more on AI and machine learning beyond this guide, my favorite book right now is Janelle Shane's '[You Look Like a Thing and I Love You](https://www.janelleshane.com/book-you-look-like-a-thing),' which informs a lot of the high-level concepts found in this guide. Thank you, Janelle!_

---

### Metaphors For What ChatGPT Can (and Can't) Do

There are a few different ways to look at ChatGPT. Here are a few metaphors to get you started:

#### ChatGPT is like a very tech-savvy intern

ChatGPT is helpful when assisting you in work that might be too repetitive or time-consuming. If you feel comfortable handing off work to ChatGPT that you also can fact-check and fine-tune on your own, you're in good hands.

#### ChatGPT is like a Rabbi, Mullah, or Priest of the Internet

If the Internet is its sacred text, ChatGPT interprets and conveys its information in a way that's easy to read and digest for as many people as possible. This communication can help visualize and break-down complicated or abstract ideas, but it should be taken with a grain of salt and not be a substitute for your own knowledge or abilities. AI is only as good and bias as the data it's trained on. ChatGPT is only as informed as the Internet allows it to be.

#### ChatGPT is like a very knowledgeable person (but not a very smart person)

ChatGPT's access to information is impressive. Still, dumb questions don't yield smart answers. ChatGPT will not be able to always figure out the intent or context of your questions unless you explicitly tell it so. This is where the famous expression "garbage in, garbage out" comes into play. The better your questions and data, the better ChatGPT can help.

#### ChatGPT is like a dog that wants to play fetch

It's very excited to play fetch with you (retrieve whatever data is needed to help you solve a problem) even if it can't understand what you're trying to do. You can train a dog to fetch a stick (like you can train an algorithm with machine learning to do a specific task), but it doesn't understand what a "stick" is like a human understands a stick; it can only understand that you want it. ChatGPT only wants a treat and be told it's a good boy. ([Janelle Shane](https://www.janelleshane.com/book-you-look-like-a-thing))

#### ChatGPT is like an impressionable child

It learns by example (like algorithms learning from data) and has _no_ idea what it should or shouldn't imitate, unless you tell it so. ([Janelle Shane](https://www.janelleshane.com/book-you-look-like-a-thing))

#### ChatGPT is NOT like C-3PO (it's more like a swarm of flies ... or a pile of worms)

[Janelle Shane](https://www.janelleshane.com/book-you-look-like-a-thing)'s five principles of "AI Weirdness" is as follows:

1. The dangers of AI is not that it's too smart ... it's that it's not smart enough.
2. AI has the approximate brainpower of a worm.
3. AI doesn't really understand the problem you want it to solve.
4. AI, however, will do _exactly_ what you tell it to do (or at least try its best).
5. AI will take the path of least resistance.

So ChatGPT is less an intelligent machine that's timid and uptight from its own knowledge and servitude and more like a bunch of well-meaning worms doing their best.

---

### Project Goals and Intended Audience

The goal of this guide is to establish foundational knowledge of ChatGPT and some basic concepts behind AI and machine learning. This could be your first-ever guide to ChatGPT, whether you've never touched code and are only using the popular chat functionality or a developer using OpenAI's API to build your first ChatGPT app.

This saying has already become cliche, and it's true: AI will probably ("probably") not take your job, but it _will_ change your job.

![image](https://doodleipsum.com/700x700?bg=D96363&i=c194787e015a971b4da76eccefb9bfa7)

## II. Getting Started <a name="getting-started"></a>

[Return to top](#top)

### System Requirements

ChatGPT

- [A free OpenAI account](https://openai.com/blog/chatgpt)
- A web browser with secure internet

> TROUBLESHOOTING: Sometimes when using ChatGPT on the web, if you don't use it after a few minutes, you'll get errors with each new prompt you try to enter. Refreshing your web browser fixes this issue.

Mac

- macOS 10.15 or later
- At least 4GB of RAM
- 2GHz Intel Core i5 or equivalent CPU

Windows:

- Windows 10 or later
- At least 4GB of RAM
- 2GHz Intel Core i5 or equivalent CPU

Linux:

- Ubuntu 18.04 or later, or a similar Linux distribution
- At least 4GB of RAM
- 2GHz Intel Core i5 or equivalent CPU

> _NOTE: For the sake of simplicity and accessibility, we're using GPT-3. GPT-4 is available but only in beta; this guide will be updated once GPT-4 and future versions are more widely available._
>
> _IMPORTANT: Be mindful of everything you send to ChatGPT. Do not share private information that you would not want ChatGPT to remember and store. Assume that everything you write to ChatGPT will eventually be hacked and printed somewhere else on the Internet._

---

### Installing Dependencies

Both chatbot examples in this guide are written in Python, so download the latest versions of the following:

- [Python](https://platform.openai.com/docs/quickstart/build-your-application) (OpenAI's docs have great info on how to get started with Python)
- [OpenAI](https://platform.openai.com/docs/api-reference/introduction) (and make sure to [create your secret API key](https://platform.openai.com/account/api-keys))
- [Gradio](https://gradio.app/quickstart/) (the UI library used to locally deploy these chatbot; any UI library is fine, though Gradio is easy to use with OpenAI.)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (to keep my secret key hidden!)

As of this writing, I'm using the API model version "gpt-3.5-turbo," though this may be updated in a future release.

> _Though this guide focuses on Python, other languages can use OpenAI's API. For example, [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A) has a great video on using ChatGPT to build a "Hello, World" React app, and [Web Dev Simplified](https://www.youtube.com/watch?v=4qNwoAAfnk4) made a great video reviewing the basics of creating a chatbot with vanilla JavaScript._

---

### Running the Code

To run the code in either `.py` file:

1. Open a new terminal.
2. Run the python command and the name of the file. (i.e `python chat_cli.py` or `python chat_ui.py`).
3. The terminal will provide next steps.

When you want to stop either program:

1. Go into the terminal where you're running the chat.
2. On your keyboard, keypress `control + c`.

![image](https://doodleipsum.com/700x700?bg=D96363&i=63ba4d9815821585ba01b47e5b6af89e)

## III. Usage <a name="usage"></a>

[Return to top](#top)

### Overview of Features

ChatGPT is unique in how much it can offer to users. Notable features include:

- **Easy integration**: you only need a few lines of code to add ChatGPT into your app. (See `chat_cli.py` and `chat_ul.py` to see this code in action.)
- **Customizable response parameters**: it's possible to control a response's length, its temperature (rate of randomness), the number of responses at a time, and more.
- **Rich responses**: ChatGPT can be flexible with the type of content it responds with, including longform prose, bullet-point lists, and code snippets.
- **Multi-turn conversations**: ChatGPT can remember previous user inputs and take them into consideration when generating new responses.

> ChatGPT is constantly changing and updating. To see all updates made so far, please refer to OpenAI's ever-evolving [release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

---

### Using `chat_cli.py` (ChatGPT in the Command Line)

This is a very simple example of how to build your own chatbot that runs in the command line with ChatGPT. The file's main feature is its `chatbot` function, which is broken down like so:

```python
message_history = []
```

We first create an empty list called `message_history` that'll store our chat's conversation. We then create a `while` loop that'll repeat until the user manually stop the app. The following code snippets live inside this `while` loop.

```python
user_input = input("USER PROMPT > ")
print(f"YOU ASKED: '{user_input}' ...")
```

We prompt the user to input data, which we store in our new variable `user_input`. Printing `user_input` confirms to the user what they entered.

```python
message_history.append({"role": "user", "content": user_input})
```

We then append our new `user_input` into `message_history`, as well as its role as a "user." We then create a `try-except` block that'll handle potential errors (more on that in a moment).

```python
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=message_history,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)
```

_This_ is how we finally begin talking to ChatGPT - by creating a `completion`. This basic `openai.ChatCompletion.create()` method includes the following:

- `model`: the specific GPT-3 language model we're using.
- `messages`: our chat history.
- `max_tokens`: the max number of tokens to generate in a response.
- `n`: the number of responses to return at a time.
- `stop`: define any specific conditions that'll stop a response.
- `temperature`: the level of randomness in a generated response (from 0 to 1, the closer to 1 - the "higher" the temperature - the more random the response)

```python
reply_content = completion.choices[0].message.content
print("CHATGPT RESPONSE:", reply_content)
```

Our new `reply_content` variable extracts and stores our API's `completion`. The API provides a lot of information, but `reply_content` is only concern with the content of the actual message. Printing `reply_content` allows the user to see the API's response and only the information they want to see.

```python
message_history.append({
  "role": "assistant",
  "content": reply_content
})
```

We then append our new `reply_content` to `message_history`, and note its role as an "assistant."

This cycle repeats until the user manually stops the app with the keypress `control + c`.

```python
except openai.error.OpenAIError as error:
  print("OpenAI API error:", error)
```

All the above code under the `try` block is executed when there are no issues. When issues do come up, this `except` block kicks in. This is an exception handler that'll print any errors to the user for future troubleshooting.

---

### Using `chat_ui.py` (ChatGPT Deployed on Localhost)

This an example of how to deploy a simple chatbot locally in your web browser. The overall structure is similar to `chat_cli.py`, but it's worth nothing this important difference:

```python
messages = [{
    "role":
    "system",
    "content":
    "You are a music curator with decades of experience in the music industry who helps people discover great new music from any era or genre. You value the classics yet always try to steer new listeners to discover music they might not have heard before."
}]
```

By defining `messages` early with this specific "system" content, we're setting the context for our chatbot. With this example, the chatbot now acts like a music curator. However, it's easy to change the system's content to set the chatbot to talk like a financial planner, or a sassy middle school teacher.

![image](https://doodleipsum.com/700x700?bg=D96363&i=62784286f00abd02f2e458828b87d767)

## IV. Examples of ChatGPT Prompts and Best Practices <a name="prompt-examples"></a>

[Return to top](#top)

There are _so_ many ways to use ChatGPT. Below are some examples I especially love and their sources as needed. Each bullet point is a prompt that you would type into ChatGPT, and each sub-bullet is a follow-up prompt that you can write in the same open window.

### General Learning, Troubleshooting, Or Brainstorming

- What are the top 3 books for learning Java? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- What are the key takeaways from Kurt Vonnegut's novel 'Slaughterhouse-Five'? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- What does the word "monozygotic" mean?
  - Now give me a synonym.
  - Now use it in 10 sentences. ([Santrel](https://youtu.be/jHv63Uvk5VA))
- How do I become a front-end developer? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I want to hire a graphic designer to design my website. We've agreed that they will deliver the first draft in two weeks and offer three iterations free of charge. Any iteration after will be charged at $50/hour. Write a contract for us. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc)) (_Make sure to run any contracts by a real-life lawyer first!_)
- Write an email to my boss asking for a raise. I've worked at this company for 2 years and successfully delivered several projects on time. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I want to learn about the fetch API. What are the steps that I should take?
  - Tell me more about #2.
  - Show me an example of the fetch API and a POST request.
  - Show me this example using async await.
  - What are some good books about the fetch API?
  - What about YouTube videos? ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- Give me some ideas for an app that uses the geolocation API.
  - Tell me more about #3. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### Creating Your Own Study Guide

- Give me a study plan to learn Python for data science with resources and a timeline. ([Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs))
- Act as a coding tutor that creates study plans to help people learn to code. You will be provided with the goal of the student, their time commitment, and resource preferences. You will create a study plan with timelines and links to resources. Only include relevant resources because time is limited. My first request: "I want to become a data scientist but I do not know how to code. I can study 10 hours per week and only want video resources. I want to learn to code in Python. Create a study plan for me." ([Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs))

---

### Generating Project Ideas

- Act as an expert data scientist and create an exploratory data analysis Python data science project about Naruto the anime. ([Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs))

---

### Preparing Your Resume For A Specific Application

- I'm applying for this role [paste in job posting URL or the text of the application] what keywords should I include on my resume?
  - I've updated my resume to include these keywords [paste in text of the updated resume] does this resume text properly incorporate the keywords of this job position? Don't mind the structure or format of the resume text.

---

### Preparing For A Job Interview

- I have three years of experience coding in HTML, CSS, and JavaScript. Write a resume for me. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I'm applying for a front-end engineer role at Netflix. Write a cover letter for me. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Act as a technical interviewer and ask me 5 questions about JavaScript
  - What is the answer to the first question? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- You are conducting an interview for a senior Front End developer role. I want you to ask me difficult React.js, HTML, CSS, and JavaScript interview questions. Your response should contain the difficulty rating, but do not give me the answer or any other information. Start by asking me one question. ([Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw))
- Can you give me an HTML question about accessibility? ([Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw))
- Explain JavaScript like I'm a 5-year-old. ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))
- What are the three most important concepts to know in React.js? ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))

---

### Working In Excel

- Write an Excel formula to add up values in cells B2 through B10.
  - Can you explain how this function works? ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to calculate the profit. The revenue is in cell A2 and the cost is in B2. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to find "Sugar Cookie" in a table and return the price.
  - Can I use any other functions? ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to extract all the text before the @ character in cell A2. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to count the number of unique values in a list. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel macro to send emails. Use the following subject: "Kevin Cookie Company Invoice." Use the following text: "You owe the Kevin Cookie Company X." Take the value X from column A. Send it to the email address listed in column B. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))

---

### Writing Shell (Linux) Commands

- Write a bash command to find the name of all jpeg files in a directory and write them all to a text file. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

---

### Writing Git Commands

- How do I know how many lines of code I've committed to a Git repository? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

---

### Improving Code & Getting Feedback

- How can I improve this code? [Then paste the code.] ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Can you provide some feedback on this code? [Then paste the code.] ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- As a senior technical writer, please review and give feedback on the README to this GitHub project: [paste in GitHub URL]. This README acts like documentation for a beginner's guide to ChatGPT. This URL includes an example of documentation that is considered "good" and which I'd like to use as a reference: [paste in URL]. This ChatGPT README should incorporate the DITA documentation concepts of Concept, Procedure/Task, and API. The README should have imperative voice and should avoid implicit voice, adverbs, and filler words that don't add any value.
  - Search this README and return any words with implicit voice, any words that are adverbs, and any filler words.

---

### Extracting Data

- Based on this Wikipedia article, when was the first Model T made? [Then paste in the article text or wiki url.]
  - Now output that as a Python variable. ([Santrel](https://youtu.be/jHv63Uvk5VA))

---

### Generating Dummy Data

- Generate dummy data for a table called Customers. Each customer should have an ID, first name, last name, and city. I don't need a Python script. Just give me the data.
  - Create a Python class for storing these objects. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I need some sample data. I need a JSON array of 10 coding bootcamps with at least 10 fields each.
  - Take out the programming languages field.
  - Give me the same data in XML. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### Generating Documentation

- Generate the documentation for this API. [Then paste in the GitHub repo URL.] ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- I need to make a glossary for a study guide I'm making on ChatGPT. What key terms should I include in this new glossary to help beginners who are new to ChatGPT, AI, and machine learning?

---

### Understanding and Fixing Errors

- Uncaught TypeError: Cannot read property 'bar' of undefined ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Can you tell me what this error message means and how to fix it? [Then paste in code and error message.] ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### Writing Tests

- Can you generate a unit test for the searchStates function using JEST? [Paste in code.] ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### Building An API

- I need an API built with Express.js to return the list of products. Each product should have attributes like ID, title, description, price, and imageURL.
  - Modify the code and retrieve the products from a MongoDB database.
  - Use TypeScript in this code.
  - Generate this API using Python and FastAPI. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

---

### Natural Language Programming

- I need a REST API built with Rust. It should have products with the fields of id, name, description, and category_id. The category_id should have a relationship with another resource called categories. Categories should have an id and a name field. Let's use an SQLite database. Use any frameworks and libraries that you see fit. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### Python Examples

- Write a python function for generating a random password.
  - What does [line of code I don't understand] do in this code?
  - What is the time complexity of this function?
  - Write unit tests for this function.
  - Convert this Python code to JavaScript. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- How can I scrape a web page using Python? ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- Give me a function to convert c to f in Python. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### HTML, CSS, and JavaScript Examples

- Write the HTML and CSS code for displaying a card. Add a button below the card content. When I hover my mouse over the card, I want the card to slightly slide up.
  - Can you rewrite this code using TailwindCSS?
  - When I click on the button, send an HTTP request to /api/products. Instead of the fetch API, use Axios. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I need the HTML and CSS in separate files for a blog homepage with a navbar with a logo on the left and links on the right. A hero area with a background image and centered text. Under that should be 3 cards in a horizontal flexbox. The cards should have light gray background and a box shadow. Use light blues and greens and use the poppies font. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

---

### React Examples

- Create a React component for displaying a card.
  - Deconstruct the props parameter. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Create a basic react component that says hello world. CODE ONLY.
  - Add a button that toggles the visibility of the text.
  - Now write a test for this app using Playwright.
  - Document this code. ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))

---

### SQL Examples

- Write an SQL query to generate a table called products with 4 columns. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Write an SQL query to generate a table called products with these columns: Id (int), Title (string), Category (int), unitPrice (float), and imageUrl (string). ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Write an SQL query to retrieve the top 5 customers in Manhattan.
  - Revise this query and join the customers table with the orders table to find out how much each customer has spent. Then pick the top 5 who have spent the most. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

![image](https://doodleipsum.com/700x700?bg=D96363&i=1d9b55f18d3b7eb28a728bd315671fb0)

## V. API Reference <a name="api-reference"></a>

[Return to top](#top)

### Overview of the OpenAI API

The good news is that OpenAI's documentation is detailed and easy to read. When in doubt, go straight to the source: <https://platform.openai.com/>

#### API Quick Links

- [OpenAI's Playground](https://platform.openai.com/playground) (to test out API completions)
- ChatGPT's API libraries:
  - [Python](https://platform.openai.com/docs/libraries/python-bindings)
  - [Node.js](https://platform.openai.com/docs/libraries/node-js-library)
  - [Community libraries (multiple languages)](https://platform.openai.com/docs/libraries/community-libraries)
- [ChatGPT Application Examples](https://platform.openai.com/examples)

---

### Obtaining an API key

After you've created an OpenAI account, head to the [API keys](https://platform.openai.com/account/api-keys) page and follow its steps. (And always keep this key safe and secret!)

---

### Examples of API usage

The OpenAI API can do a lot of various things - it's a powerful tool meant to be used for a wide range of problems. OpenAI's [Examples](https://platform.openai.com/examples) page includes a long list of example applications that use ChatGPT in different use cases. Some overall categories of these examples include:

- **Language tasks**: generating prose, summarizing documents, and translating text between languages.
- **Conversational AI**: create chatbots (which we do in our example Python files in this guide), virtual assistants, and customer support systems.
- **Content creation**: generate articles, blog posts, and product descriptions.
- **Data analysis**: analyze large datasets and extract insights.
- **Productivity tools**: automate tedious tasks or decision making like to-do lists, writing emails, or even playing chess.

![image](https://doodleipsum.com/700x700?bg=D96363&i=c0d1afba2fed7fef82cfc60fbf999cf7)

## VI. Giving Thanks <a name="legal"></a>

[Return to top](#top)

### Closing Credits

A shout-out to [Nick Arocho](https://www.nickarocho.com/) for his initial guidance on where to get started with ChatGPT. Videos by [The AI Advantage](https://www.youtube.com/watch?v=pGOyw_M1mNE) and [sentdex](https://www.youtube.com/watch?v=c-g6epk3fFE) helped me get started with ChatGPT's API in Python and Gradio. Doodles by [Doodle Ipsum](https://doodleipsum.com/). And again, [Janelle Shane's book](https://www.janelleshane.com/book-you-look-like-a-thing) is a must-read.

---

### Cited Sources

The following videos were vital in helping me make this guide. For further learning, I encourage you to watch these videos by these creators:

- [Traversy](https://www.youtube.com/watch?v=o_joulYVndM)
- [Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc)
- [Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s)
- [Santrel](https://youtu.be/jHv63Uvk5VA)
- [Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs)
- [Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw)
- [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A)
- [Beyond Fireship](https://www.youtube.com/watch?v=e2uvhJ7r1UQ)

![image](https://doodleipsum.com/700/flat?bg=D96363&i=34b1669d12f4f37be2f8fda91b87b784)

## VII. Glossary <a name="glossary"></a>

[Return to top](#top)

### Artificial Intelligence (AI)

The ability of machines to perform tasks that would typically require human intelligence, such as learning, problem-solving, and decision-making.

### Machine Learning

A subfield of AI that involves training machines to learn from data, so they can make predictions or decisions without being explicitly programmed.

### Natural Language Processing (NLP)

A subfield of AI that focuses on the interaction between machines and humans using natural language, such as speech or text.

### Chatbot

A computer program that uses NLP to simulate conversation with human users, typically through messaging applications or voice assistants.

### Deep Learning

A subfield of machine learning that involves training neural networks with many layers to recognize patterns in data.

### Neural Network

A type of machine learning algorithm that is modeled after the structure of the human brain and consists of interconnected nodes or neurons that process information.

### Generative Model

A type of AI model that generates new data that is similar to the training data it was trained on, such as text or images.

### Transformer Model

A type of neural network that is widely used for NLP tasks, such as language translation, text summarization, and question answering.

### API (Application Programming Interface)

A set of rules and protocols that allows different software applications to communicate with each other. In the context of this project, it refers to the programming interface provided by ChatGPT that allows developers to integrate the model into their own applications.

---

© 2023 Brady Gerber. All Rights Reserved.

[Return to top](#top)
