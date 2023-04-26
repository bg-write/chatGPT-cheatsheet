<a name="top"></a>

# ChatGPT Cheatsheet

Learn how to use ChatGPT's prompt portal and API, whether you're new to AI or trying to build your first chatbot.

_Version 1.1.0: Updated outline to split documentation into three overall parts with introduction._

[![GitHub issues](https://img.shields.io/github/issues/bg-write/chatGPT-cheatsheet?style=flat-square)](https://github.com/bg-write/chatGPT-cheatsheet/issues)

![image](https://doodleipsum.com/700x700?bg=D96363&i=7bba2d304a189734c2a8226c512748dd)

## The TL;DR

- _ChatGPT, and AI in general, is less like C-3PO and more like a bunch of well-meaning worms doing their best._
- _After a high-level introduction, this guide divides into sections for just using the prompt portal ([Part A](#part-a)) and then using the actual API ([Part B](#part-b)). [Part C](#part-c) is a reference for all users._
- _AI is only as good as the data it's trained on. The better and more specific your prompt and parameters, the more helpful ChatGPT can be._
- _Avoid sharing any private or sensitive data. Assume that everything you write to ChatGPT will eventually be hacked and printed somewhere on the Internet._

---

## Table of Contents

I. [Introduction](#intro)

- Overview of ChatGPT
- How You Can Use ChatGPT
- Metaphors For What ChatGPT Can (and Can't) Do
- Guide Goals and Intended Audience

### [PART A: ChatGPT's Prompt Portal](#part-a)

II. [Getting Started (Prompt Portal)](#getting-started-prompt)

- Step-by-Step Guide
- Writing Your First Prompt
- The Art of a Good Prompt

III. [Examples of ChatGPT Prompts](#prompt-examples)

- General Learning, Troubleshooting, Or Brainstorming
- Editing, Summarizing, and Translating Text
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

### [PART B: ChatGPT's API](#part-b)

IV. [Getting Started (ChatGPT's API)](#getting-started-api)

- System Requirements
- Installing Dependencies
- Running the Code

V. [Usage](#usage)

- Overview of API Features
- Using `chat_cli.py` (ChatGPT in the Command Line)
- Using `chat_ui.py` (ChatGPT Deployed on Localhost)

VI. [API Reference](#api-reference)

- API Documentation & Quick Links
- Obtaining an API key
- API Example Applications

### [PART C: Conclusion & References](#part-c)

VII. [Giving Thanks](#legal)

- Closing Credits
- Cited Sources

VIII. [Glossary](#glossary)

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

**Natural language processing models** are AI models that enable computers to understand, interpret, and generate human language, allowing them to interact with humans through speech or text. There are many types of AI models (more details to come in a future version of this guide). For now, it's important to know that ChatGPT uses the **Transformer** model. Compared to other AI models, the Transformer model is better at generating responses that focus on the _context_ of a conversation. What makes ChatGPT special is that it can be picky and focus on the most relevant parts of a user's input instead of having to process an entire sequence at once.

> _If you'd like to read more on AI and machine learning beyond this guide, my favorite book right now is Janelle Shane's '[You Look Like a Thing and I Love You](https://www.janelleshane.com/book-you-look-like-a-thing),' which informs a lot of the high-level concepts found in this guide. Thank you, Janelle!_

---

### How You Can Use ChatGPT

For non-developers:

- **Ask** questions or give commands to ChatGPT to then take specific actions and steps.
  - i.e. Explain JavaScript like I'm a 5-year-old, and then explain it to me like I'm a senior engineer.
- **Generate** ideas, documentation, or dummy data.
  - i.e. I need some sample data. I need a JSON array of 10 colleges with at least 10 fields each.
- **Extract** summaries, key words, and other data from text, links, or other online resources.
  - i.e. I'm applying for this role [paste in job posting URL or text] what keywords should I include on my resume?
- **Draft** personalized study guides for future learning.
  - i.e. Give me a study plan to learn Python for data science within a month with free video resources.
- **Create** first drafts of various text content.
  - i.e. I have three years of experience coding in HTML, CSS, and JavaScript. Write a resume for me.
- **Present** high-level or technical problems and ask ChatGPT for potential solutions and examples.
  - i.e. Write an Excel formula to add up values in cells B2 through B10.
- **Refine** text or code with specific goals.
  - i.e. Here is my resume [paste in text] do you spot any typos? If so, please list them.
- And more!

For software engineers:

- **Develop** chatbots for customer service or sales.
- **Create** virtual assistants for personal or business use.
- **Integrate** ChatGPT with NLP tools to automate tasks.
- **Generate** actual content drafts for marketing or advertising campaigns.
- And more!

---

### Metaphors For What ChatGPT Can (and Can't) Do

There are a few different ways to approach ChatGPT. Here are a few metaphors to get you started:

#### ChatGPT is like a very tech-savvy intern

ChatGPT is helpful when assisting you in work that might be too repetitive or time-consuming. If you feel comfortable handing off work to ChatGPT that you also can fact-check and fine-tune on your own, you're in good hands. And though interns are so helpful, we still need to review the results before putting them into practice; if you submit your work and something goes wrong, do you want to tell your boss that "Well, that's what ChatGPT gave me"?

#### ChatGPT is like a Rabbi, Mullah, or Priest of the Internet

If the Internet is its sacred text, ChatGPT interprets and conveys its information in a way that's easy to read and digest for as many people as possible. This communication can help visualize and break-down complicated or abstract ideas. It should also be taken with a grain of salt and not be a substitute for your own knowledge or abilities. AI is only as good and bias as the data it's trained on. ChatGPT is only as informed as the Internet allows it to be.

#### ChatGPT is like a very knowledgeable person (but not a very smart person)

ChatGPT's access to information is impressive. Still, dumb questions don't yield smart answers. ChatGPT will not be able to always figure out the intent or context of your questions unless you explicitly tell it so. This is where the famous expression "garbage in, garbage out" comes into play. The better your questions and data, the better ChatGPT can help.

#### ChatGPT is like a dog that wants to play fetch

It's very excited to play fetch with you (retrieve whatever data is needed to help you solve a problem) but it can't understand what you're trying to do. You can train a dog to fetch a stick (like you can train an algorithm with machine learning to do a specific task), but it doesn't understand what a "stick" is like a human understands a stick; it can only understand that you want "stick." ChatGPT only wants a treat and to be told it's a good boy. ([Janelle Shane](https://www.janelleshane.com/book-you-look-like-a-thing))

#### ChatGPT is like an impressionable child

It learns by example (like algorithms learning from data) and has _no_ idea what it should or shouldn't imitate, unless you tell it so. ([Janelle Shane](https://www.janelleshane.com/book-you-look-like-a-thing))

#### ChatGPT is NOT like C-3PO (it's more like a swarm of flies ... or a pile of worms)

[Janelle Shane](https://www.janelleshane.com/book-you-look-like-a-thing)'s five principles of "AI Weirdness":

1. The dangers of AI is not that it's too smart ... it's that it's not smart enough.
2. AI has the approximate brainpower of a worm.
3. AI doesn't really understand the problem you want it to solve.
4. AI, however, will do _exactly_ what you tell it to do (or at least try its best).
5. AI will take the path of least resistance.

So ChatGPT is less an intelligent machine that's timid and uptight from its own knowledge and servitude and more like a bunch of well-meaning worms doing their best.

---

### Guide Goals and Intended Audience

The goal of this guide is to establish foundational knowledge of ChatGPT and some basic concepts behind AI and machine learning.

This could be your first-ever guide to ChatGPT, whether you've never touched code and are only using the popular chat functionality or a developer using the API to build your first ChatGPT app.

This saying has already become cliche, and it's true: AI will probably ("probably") not take your job, but it _will_ change your job.

> _NOTE: For the sake of simplicity and accessibility, we're using GPT-3. GPT-4 is available but only in beta. This guide will be updated once GPT-4 and future versions are more widely available._
>
> _IMPORTANT: Be mindful of everything you send to ChatGPT. Do not share private information that you would not want ChatGPT to remember and store. Assume that everything you write to ChatGPT will eventually be hacked and printed somewhere else on the Internet._

![image](https://doodleipsum.com/700x700?bg=D96363&i=c194787e015a971b4da76eccefb9bfa7)

## PART A: ChatGPT's Prompt Portal <a name="part-a"></a>

This section provides a beginner's guide to ChatGPT for non-developers and software engineers who want to use ChatGPT's prompt portal to generate responses to their text inputs.

## II. Getting Started (Prompt Portal) <a name="getting-started-prompt"></a>

[Return to top](#top)

### Step-by-Step Guide

All you need to get started is a free OpenAI account:

1. Sign up for [OpenAI](https://openai.com/blog/chatgpt).
2. Access the prompt portal.
3. Enter your text input.
4. Watch ChatGPT generate its output.

> TROUBLESHOOTING: Sometimes when using ChatGPT on the web, if you don't use it after a few minutes, you'll get errors with each new prompt you try to enter. Refreshing your web browser fixes this issue.

---

### Writing Your First Prompt

All you have to do is write your prompt in the "Send a message" text box, press enter, and watch ChatGPT respond. It's that easy!

> Try entering this prompt to start: "Tell me a dad joke."

---

### The Art of a Good Prompt

ChatGPT is only as good as your prompt. Here are some starting tips on writing good prompts:

- Keep your prompt clear and concise.
- Ask a specific question or give a clear command. Don't write something broad or open-ended.
- Provide context for your prompt; ChatGPT will not be able to pick this up on its own.
- Use correct grammar and spelling.
- Avoid biased or discriminatory language.

#### A Bad Prompt

Where to eat in Chi.

#### An OK Prompt

Can you recommend any good restaurants in Chicago?

#### A Good Prompt

I'm visiting Chicago for the first time this summer and am looking for some great places to eat. Specifically, I'm interested in seafood and italian cuisine. Do you have any recommendations for restaurants that fit this criteria? The closer these recommendations are to mass transit, the better. I don't want to spend more than $100 on a meal if possible.

![image](https://doodleipsum.com/700/flat?bg=D96363&i=f0680f8b2b8802c8321a580f63ec3d40)

## III. Examples of ChatGPT Prompts <a name="prompt-examples"></a>

[Return to top](#top)

There are _so_ many ways to use ChatGPT. Below are some real examples and their sources as needed. Each bullet point is a prompt that you would type into ChatGPT, and each sub-bullet is a follow-up prompt that you can write in the same open window.

### General Learning, Troubleshooting, Or Brainstorming

- What are the top 3 books for learning Java? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- List 10 science fiction books. ([OpenAI](#api-reference))
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

### Editing, Summarizing, and Translating Text

- Correct this to standard English: [Paste in text you wish to correct]. ([OpenAI](#api-reference))
- Summarize this for a second-grade student: [Paste in text you wish to summarize]. ([OpenAI](#api-reference))
- Translate this into 1. French, 2. Spanish and 3. Japanese: What rooms do you have available? ([OpenAI](#api-reference))
- Convert movie titles into emoji: Back to the Future, Batman, Transformers, and Star Wars. ([OpenAI](#api-reference))
- A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei. Tl;dr. ([OpenAI](#api-reference))
- Create an analogy for this phrase: Questions are like arrows. ([OpenAI](#api-reference))
- Convert this from first-person to third person (gender female): I decided to make a movie about Ada Lovelace. ([OpenAI](#api-reference))

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
- Give the background-color CSS code for a color like a blue sky at dusk. ([OpenAI](#api-reference))

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

## PART B: ChatGPT's API <a name="part-b"></a>

This section provide a beginner's guide to ChatGPT for software engineers who want to integrate ChatGPT's AI into their own applications.

## IV. Getting Started (ChatGPT's API) <a name="getting-started-api"></a>

[Return to top](#top)

### System Requirements

ChatGPT

- [A free OpenAI account](https://openai.com/blog/chatgpt)
- [Secret API key](https://platform.openai.com/account/api-keys)

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

---

### Installing Dependencies

Both chatbot examples in this guide are written in Python, so download the latest version of the following:

- [Python](https://platform.openai.com/docs/quickstart/build-your-application) (OpenAI's docs have great information on how to get started with Python)
- [OpenAI](https://platform.openai.com/docs/api-reference/introduction) (and make sure to [create your secret API key](https://platform.openai.com/account/api-keys))
- [Gradio](https://gradio.app/quickstart/) (the UI library used to locally deploy these chatbot; any UI library is fine, though Gradio is easy to use with OpenAI)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (to keep the secret key hidden!)

As of this writing, this guide is using the API model version "gpt-3.5-turbo," though this may be updated in a future release.

> _Though this guide focuses on Python, other languages can use OpenAI's API. For example, [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A) has a great video on using ChatGPT to build a "Hello, World" React app, and [Web Dev Simplified](https://www.youtube.com/watch?v=4qNwoAAfnk4) made a great video reviewing the basics of creating a chatbot with vanilla JavaScript._

---

### Running the Code

This GitHub includes the Python files `chat_cli.py` and `chat_ui.py`. These are simple examples that we'll use to visualize ChatGPT's API in action. To run the code in either `.py` file:

1. Open a new terminal.
2. Run the python command and the name of the file. (i.e `python chat_cli.py` or `python chat_ui.py`).
3. The terminal will provide next steps.

When you want to stop either program:

1. Go into the terminal where you're running the chat.
2. On your keyboard, keypress `control + c`.

![image](https://doodleipsum.com/700x700?bg=D96363&i=63ba4d9815821585ba01b47e5b6af89e)

## V. Usage <a name="usage"></a>

[Return to top](#top)

This section introduces the actual use of ChatGPT's API and reviews our beginner examples found in `chat_cli.py` and `chat_ui.py`. We'll explore these concepts even further in the [API Reference](#api-reference) section.

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
- `temperature`: the level of randomness in a generated response (from 0 to 1, the closer to 1 - the "higher" the temperature - the more random the response).

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

## VI. API Reference <a name="api-reference"></a>

[Return to top](#top)

OpenAI's documentation is very detailed and easy to navigate. This section is a breakdown of ChatGPT's overall documentation (sections "Get started," "Guides," and "Chat Plugins") with related links.

---

### API Documentation & Quick Links

 When in doubt, you can always go straight to the source and explore from there: <https://platform.openai.com/>

For the scope of this guide, it's best to start with these documentation sections:

1. [Introduction](https://platform.openai.com/docs/introduction)
2. [Quickstart](https://platform.openai.com/docs/quickstart)
3. [Text completion](https://platform.openai.com/docs/guides/completion)
4. [Chat completion](https://platform.openai.com/docs/guides/chat)

#### Get started

- [Introduction](https://platform.openai.com/docs/introduction)
  - Overview
  - Key concepts: Prompts, Tokens, and Models
  - Next steps
- [Quickstart](https://platform.openai.com/docs/quickstart)
  - Introduction: An intro to "Completion"
  - Start with an instruction
  - Add some examples
  - Adjust your settings: An intro to "Temperature"
  - Build your application (Node.js or Python/Flask)
  - Pricing
  - Closing
  - Next steps
- [Libraries](https://platform.openai.com/docs/libraries)
  - Python
  - Node.js
  - Community libraries (multiple languages)
- [Models](https://platform.openai.com/docs/models/overview)
  - Overview
  - Model compatibility: API endpoints and model names
  - Model updates
  - GPT-4 (limited beta)
  - GPT-3.5
  - DALL-E (beta): generate and edit images using NLP
  - Whisper (beta): convert audio into text
  - Embeddings: convert text into a numerical form
  - Moderation: detection of sensitive or unsafe text
  - GPT-3
- [Tutorials](https://platform.openai.com/docs/tutorials)
  - Website Q&A with Embeddings

#### Guides

- [Text completion](https://platform.openai.com/docs/guides/completion)
  - Introduction
  - Prompt design: showing and telling, providing quality data, checking your settings, and more
  - Inserting text
  - Editing text
- [Chat completion](https://platform.openai.com/docs/guides/chat)
  - Introduction: examples of the API response format and managing tokens
  - Instructing chat models
  - Chat vs Completions
  - FAQ
- [Image generation w/ DALL-E](https://platform.openai.com/docs/guides/images/introduction)
  - Introduction
  - Usage: Generations, Edits, and Variations
  - Language-specific tips: Node.js, TypeScript, and error handling
- [Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)
  - Preparing your dataset
  - Advanced usage
  - Weights & Biases
  - Example notebooks: Classification and Question answering
- [Embeddings](https://platform.openai.com/docs/guides/embeddings)
  - Overview
  - Use cases
  - Limitations & risks
- [Speech to text w/ Whisper](https://platform.openai.com/docs/guides/speech-to-text)
  - Overview
  - Quickstart: Transcriptions and Translations
  - Supported languages
  - Longer inputs
  - Prompting
- [Moderation](https://platform.openai.com/docs/guides/moderation)
  - Overview
  - Quickstart
- [Rate limits](https://platform.openai.com/docs/guides/rate-limits)
  - Overview
  - Error mitigation
  - Rate limit increase
- [Error codes](https://platform.openai.com/docs/guides/error-codes)
  - API errors: 401, 429, and 500
  - Python library errors
- [Safety best practices](https://platform.openai.com/docs/guides/safety-best-practices)
  - The Moderation API
  - Adversarial testing
  - Human in the loop (HITL)
  - Prompt engineering
  - Know your customer (KYC)
  - Constrain user input and limit output tokens
  - Allow users to report issues
  - Understand and communicate limitations
  - End-user IDs
- [Production best practices](https://platform.openai.com/docs/guides/production-best-practices)

#### Chat Plugins (limited alpha)

- [Introduction](https://platform.openai.com/docs/plugins/introduction)
- [Getting Started](https://platform.openai.com/docs/plugins/getting-started)
- [Authentication](https://platform.openai.com/docs/plugins/authentication)
- [Examples](https://platform.openai.com/docs/plugins/examples)
- [Production](https://platform.openai.com/docs/plugins/production)
- [Plugin review](https://platform.openai.com/docs/plugins/review)

#### Other Helpful Links

- [OpenAI Terms & Policies](https://openai.com/policies)
- [Open AI Plugin policies](https://openai.com/policies/usage-policies#plugin-policies)
- [API Completion Playground](https://platform.openai.com/playground)
- [GPT comparison tool](https://gpttools.com/comparisontool)

---

### Obtaining an API key

After you've created an OpenAI account, head to the [API keys](https://platform.openai.com/account/api-keys) page and follow its steps. (And always keep this key safe and secret!)

---

### API Example Applications

ChatGPT's API is a powerful tool that can address a wide range of problems. OpenAI's [Examples](https://platform.openai.com/examples) page includes a long list of example applications that use ChatGPT in different use cases. Here are some popular examples:

#### Answering & Conversing

- [Q&A](https://platform.openai.com/examples/default-qa): Answer questions based on existing knowledge.
- [Factual answering](https://platform.openai.com/examples/default-factual-answering): Direct the model to provide factual answers and address knowledge gaps.
- [JavaScript helper chatbot](https://platform.openai.com/examples/default-js-helper): Message-style bot that answers JavaScript questions.
- [ML/AI language model tutor](https://platform.openai.com/examples/default-ml-ai-tutor): Bot that answers questions about language models.
- [Friend chat](https://platform.openai.com/examples/default-friend-chat): Emulate a text message conversation.
- [Chat](https://platform.openai.com/examples/default-chat): Open ended conversation with an AI assistant.
- [Marv the sarcastic chat bot](https://platform.openai.com/examples/default-marv-sarcastic-chat): Marv is a factual chatbot that is also sarcastic.

#### Classifying & Extracting

- [Classification](https://platform.openai.com/examples/default-classification): Classify items into categories via example.
- [Advanced tweet classifier](https://platform.openai.com/examples/default-adv-tweet-classifier): Advanced sentiment detection for a piece of text.
- [Keywords](https://platform.openai.com/examples/default-keywords): Extract keywords from a block of text.
- [Tweet classifier](https://platform.openai.com/examples/default-tweet-classifier): Basic sentiment detection for a piece of text.
- [Airport code extractor](https://platform.openai.com/examples/default-airport-codes): Extract airport codes from text.
- [Extract contact information](https://platform.openai.com/examples/default-extract-contact-info): Extract contact information from a block of text.

#### Coding & Translating

- [Grammar correction](https://platform.openai.com/examples/default-grammar): Corrects sentences into standard English.
- [English to other languages](https://platform.openai.com/examples/default-translate): Translates English text into French, Spanish and Japanese.
- [Summarize for a 2nd grader](https://platform.openai.com/examples/default-summarize): Translate difficult text into simpler concepts.
- [Natural language to OpenAI API](https://platform.openai.com/examples/default-openai-api): Create code to call to the OpenAI API using a natural language instruction.
- [Natural language to Stripe API](https://platform.openai.com/examples/default-stripe-api): Create code to call the Stripe API using natural language.
- [SQL translate](https://platform.openai.com/examples/default-sql-translate): Translate natural language to SQL queries.
- [Python to natural language](https://platform.openai.com/examples/default-python-to-natural-language): Explain a piece of Python code in human understandable language.
- [Calculate Time Complexity](https://platform.openai.com/examples/default-time-complexity): Find the time complexity of a function.
- [Translate programming languages](https://platform.openai.com/examples/default-translate-code): Translate from one programming language to another.
- [Explain code](https://platform.openai.com/examples/default-explain-code): Explain a complicated piece of code.
- [Python bug fixer](https://platform.openai.com/examples/default-fix-python-bugs): Find and fix bugs in source code.
- [JavaScript to Python](https://platform.openai.com/examples/default-js-to-py): Convert simple JavaScript expressions into Python.
- [Write a Python docstring](https://platform.openai.com/examples/default-python-docstring): Write a docstring for a Python function.
- [JavaScript one line function](https://platform.openai.com/examples/default-js-one-line): Turn a JavaScript function into a one liner.
- [Text to command](https://platform.openai.com/examples/default-text-to-command): Translate text into programmatic commands.
- [Parse unstructured data](https://platform.openai.com/examples/default-parse-data): Create tables from long form text.
- [SQL request](https://platform.openai.com/examples/default-sql-request): Create simple SQL queries.

#### Generating & Transforming

- [Movie to Emoji](https://platform.openai.com/examples/default-movie-to-emoji): Convert movie titles into emoji.
- [Ad from product description](https://platform.openai.com/examples/default-ad-product-description): Turn a product description into ad copy.
- [Product name generator](https://platform.openai.com/examples/default-product-name-gen): Create product names from examples words.
- [TL;DR summarization](https://platform.openai.com/examples/default-tldr-summary): Summarize text by adding a 'tl;dr:' to the end of a text passage.
- [Spreadsheet creator](https://platform.openai.com/examples/default-spreadsheet-gen): Create spreadsheets of various kinds of data.
- [Science fiction book list maker](https://platform.openai.com/examples/default-sci-fi-book-list): Create a list of items for a given topic.
- [Mood to color](https://platform.openai.com/examples/default-mood-color): Turn a text description into a color.
- [Analogy maker](https://platform.openai.com/examples/default-analogy-maker): Create analogies.
- [Micro horror story creator](https://platform.openai.com/examples/default-micro-horror): Creates two to three sentence short horror stories from a topic input.
- [Third-person converter](https://platform.openai.com/examples/default-third-person): Converts first-person POV to the third-person.
- [Notes to summary](https://platform.openai.com/examples/default-notes-summary): Turn meeting notes into a summary.
- [VR fitness idea generator](https://platform.openai.com/examples/default-vr-fitness): Create ideas for fitness and virtual reality games.
- [Essay outline](https://platform.openai.com/examples/default-essay-outline): Generate an outline for a research topic.
- [Recipe creator](https://platform.openai.com/examples/default-recipe-generator): Create a recipe from a list of ingredients.
- [Turn by turn directions](https://platform.openai.com/examples/default-turn-by-turn-directions): Convert natural language to turn-by-turn directions.
- [Restaurant review creator](https://platform.openai.com/examples/default-restaurant-review): Turn a few words into a restaurant review.
- [Create study notes](https://platform.openai.com/examples/default-study-notes): Provide a topic and get study notes.
- [Interview questions](https://platform.openai.com/examples/default-interview-questions): Create interview questions.

![image](https://doodleipsum.com/700x700?bg=D96363&i=c0d1afba2fed7fef82cfc60fbf999cf7)

## PART C: Conclusion & References <a name="part-c"></a>

This section provides credits, cited sources, and a glossary for both non-developers and software engineers.

## VII. Giving Thanks <a name="legal"></a>

[Return to top](#top)

### Closing Credits

A shout-out to [Nick Arocho](https://www.nickarocho.com/) for his initial guidance on where to get started with ChatGPT. Videos by [The AI Advantage](https://www.youtube.com/watch?v=pGOyw_M1mNE) and [sentdex](https://www.youtube.com/watch?v=c-g6epk3fFE) helped me get started with ChatGPT's API in Python and Gradio. Doodles by [Doodle Ipsum](https://doodleipsum.com/). And again, [Janelle Shane's book](https://www.janelleshane.com/book-you-look-like-a-thing) is a must-read.

---

### Cited Sources

The following videos were vital in helping me make this guide. For further learning, I encourage you to watch these videos by the following creators:

- [Traversy](https://www.youtube.com/watch?v=o_joulYVndM)
- [Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc)
- [Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s)
- [Santrel](https://youtu.be/jHv63Uvk5VA)
- [Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs)
- [Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw)
- [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A)
- [Beyond Fireship](https://www.youtube.com/watch?v=e2uvhJ7r1UQ)

![image](https://doodleipsum.com/700/flat?bg=D96363&i=34b1669d12f4f37be2f8fda91b87b784)

## VIII. Glossary <a name="glossary"></a>

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
