<a name="top"></a>

# ChatGPT, AI & Machine Learning: How to Get Started (and Not Be Afraid)

[![GitHub issues](https://img.shields.io/github/issues/bg-write/chatGPT-cheatsheet?style=flat-square)](https://github.com/bg-write/chatGPT-cheatsheet/issues)

![ChatGPT 101](https://doodleipsum.com/700/flat?i=dc8797cdd78c30bd8c72a5fbf1157b7e)

## Table of Contents

- What to Know Before Getting Started (Who is This Guide For?)
- AI Overview
- Machine Learning Overview
- ChatGPT Overview
- Getting Started With ChatGPT (On Your Computer)
- ChatGPT For Newbies
- ChatGPT's API (For Developers)
- Closing Credits

---

## What to Know Before Getting Started (Who is This Guide For?)

[Return to top](#top)

### ChatGPT Explained in One Sentence (to a Newbie)

ChatGPT is a computer grogram that can understand and generate human-like language to have conversations with people.

(NOTE: This is the answer I got when I asked ChatGPT to explain itself in one sentence to someone who knows nothing about ChatGPT or AI.)

### ChatGPT Explained in One Sentence (to an Experienced Engineer)

ChatGPT is a state-of-the-art, large-scale natural language processing model based on the Transformer architecture, which can generate human-like text and perform various language-related tasks with high accuracy.

(This time, I asked ChatGPT to sum itself up in one sentence to someone already experienced in AI and machine learning. Pretty cool, right?)

### ChatGPT (and AI and Machine Learning) Explained in One Minute

**AI (Artificial Intelligence)** is a type of computer technology that allows machines to perform tasks that normally require human intelligence.

**Machine Learning** is a subset of AI that enables machines to learn from data and improve their performance without being explicitly programmed.

**ChatGPT** is a particular machine learning model that has been trained on a large corpus of text data to generate human-like responses and carry out natural language processing tasks.

<!-- ### The Problem

TBD

### The Solution

TBD

### The Goal

TBD -->

### The Ideal User of This Guide

Someone interested in learning the basics of AI, Machine Learning, and ChatGPT, even out of the fear that if you don't learn it, you'll lose your job. (More on that in the next paragraph.)

### Why You Should Learn the Basics of AI (Even if You Don't Code or Care)

ChatGPT is incredible at creating many different types of content. If your current job involves creating or editing any kind of content, becoming comfortable with AI (and knowing its strengths and weaknesses) can only help you. It's already a cliche and it's true: AI will not eliminate your job, but it will likely change your job.

### Why Was This Repo Written in Python?

Python is one of my favorite languages! Python also works well with a lot of data analysis and machine learning examples that I'll be using in this guide.

### Can I Use ChatGPT with JavaScript or other languages?

Yes, [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A) did a great video on using ChatGPT to build a "Hello, World" React app. You can use ChatGPT with any language!

### Will This Repo be Outdated by the Time I Read This?

In some ways, yes. I'll try to keep this guide as updated as possible. The goal, however, is to introduce high-level concepts to ChatGPT that will remain consistent with each new release. I'll try to note when there are important differences to know between versions.

To see all updates added to ChatGPT so far, please refer to its release notes: <https://help.openai.com/en/articles/6825453-chatgpt-release-notes>

![ChatGPT 101](https://doodleipsum.com/700?i=934094fdf9650619886d1f1d9e713132)

## AI Overview

[Return to top](#top)

TBD

---

## Machine Learning Overview

[Return to top](#top)

TBD

---

## ChatGPT Overview

[Return to top](#top)

TBD

![ChatGPT 101](https://doodleipsum.com/700?i=ac5fcbd004e4a4496dc975c10f7af6be)

## Getting Started With ChatGPT (On Your Computer)

[Return to top](#top)

OpenAI's ChatGPT Home Page: <https://openai.com/blog/chatgpt>

ChatGPT's Landing Page (you'll need to log in with your OpenAI account or sign up for free): <https://chat.openai.com/auth/login>

### What ChatGPT Version am I Using?

For simplicity sake, I'm sticking to the free GPT-3. GPT-4 is the advanced paid version, but this guide focuses on the very basics for newcomers. (NOTE: We'll be using GPT-4 in the section "ChatGPT For Developers," but that section is still being written!)

![ChatGPT 101](https://doodleipsum.com/700?i=c4ede553eeb0e7df9f4e8b16bd8cae24)

## ChatGPT For Newbies

[Return to top](#top)

### Two Metaphors to Help Visualize What ChatGPT Can (and Can't) Do

- ChatGPT is like **a very tech-savvy intern**. It's helpful when assisting you in work that you can do yourself but might be too repetitive or time-consuming. If you feel comfortable handing off work to ChatGPT that you can also fact-check on your own, you're in good hands.
- If a tool or language's documentation is like its sacred text, ChatGPT is like its **pastor or priest** who interprets and conveys the text (and should only be taken with a grain of salt).

### How NOT to Use ChatGPT

- Ask for code snippets ... only to then copy and paste it into your project
- When you have no questions; ChatGPT doesn't respond well to statements.

### How TO Use ChatGPT

- Write your prompt in the form of a question or request.
- Ask for basic code as a reference (but again, don't copy and paste).
- Ask to review your code.
- Ask to quiz you on your knowledge of any specific tools or languages.
- Give it coding challenges or interview questions. (NOTE: avoid doing this during an interview, unless you've been given an explicit OK to use ChatGPT.)

### ChatGPT Prompt Categories & Example to Get You Started (with Sources)

#### General Learning, Troubleshooting, or Brainstorming

- What are the top 3 books for learning Java? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- What are the key takeaways from BOOK? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- How do I become a front-end developer? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I want to hire a graphic designer to design my website. We've agreed that they will deliver the first draft in two weeks and offer three iterations free of charge. Any iteration after will be charged at $50/hour. Write a contract for us. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc)) (Obviously run any contracts you'll actually use by a real-life lawyer first.) ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Write an email to my boss asking for a raise. I've worked at this company for 2 years and successfully delivered several projects on time. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I want to learn about the fetch API. What are the steps that I should take?
  - Tell me more about #2.
  - Show me an example of the fetch API and a POST request.
  - Show me this example using async await.
  - What are some good books about the fetch API?
  - What about YouTube videos? ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- Give me some ideas for an app that uses the geolocation API.
  - Tell me more about #3. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Preparing For A Job Interview

- I have three years of experience coding in HTML, CSS, and JavaScript. Write a resume for me. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I'm applying for a front-end engineer role at COMPANY. Write a cover letter for me. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Act as a technical interviewer and ask me 5 questions about JavaScript
  - What is the answer to the first question? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- You are conducting an interview for a senior Front End developer role. I want you to ask me difficult React.js, HTML, CSS, and JavaScript interview questions. Your response should contain the difficulty rating, but do not give me the answer or any other information. Start by asking me one question. ([Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw))
- Can you give me an HTML question about accessibility? ([Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw))
- Explain JavaScript like I'm a 5-year-old. ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))
- What are the three most important concepts to know in React.js? ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))

#### Writing Shell (Linux) Commands

- Write a bash command to find the name of all jpeg files in a directory and write them all to a text file. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

#### Writing Git Commands

- How do I know how many lines of code I've committed to a Git repository? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

#### Improving Code & Getting Feedback

- How can I improve this code? [Then paste code.] ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Can you provide some feedback on this code (then paste the code). ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Generating Dummy Data

- Generate dummy data for a table called Customers. Each customer should have an ID, first name, last name, and city. I don't need a Python script. Just give me the data.
  - Create a Python class for storing these objects. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I need some sample data. I need a JSON array of 10 coding bootcamps with at least 10 fields each.
  - Take out the programming languages field.
  - Give me the same data in XML. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Generating Documentation

- Generate the documentation for this API [paste GitHub repo URL]. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Understanding and Fixing Errors

- Uncaught TypeError: Cannot read property 'bar' of undefined ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Can you tell me what this error message means and how to fix it? [paste code and error message.] ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Writing Tests

- Can you generate a unit test for the searchStates function using JEST? [Paste in code.] ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Building an API

- I need an API built with Express.js to return the list of products. Each product should have attributes like ID, title, description, price, and imageURL.
  - Modify the code and retrieve the products from a MongoDB database
  - Use TypeScript in this code
  - Generate this API using Python and FastAPI ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

#### Natural Language Programming

- I need a REST API built with Rust. It should have products with the fields of id, name, description, and category_id. The category_id should have a relationship with another resource called categories. Categories should have an id and a name field. Let's use an SQLite database. Use any frameworks and libraries that you see fit. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Python Examples

- Write a python function for generating a random password
  - What does [line of code I don't understand] do in this code?
  - What is the time complexity of this function?
  - Write unit tests for this function.
  - Convert this Python code to JavaScript. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- How can I scrape a web page using Python? ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- Give me a function to convert c to f in Python. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### HTML, CSS, and JavaScript Examples

- Write the HTML and CSS code for displaying a card. Add a button below the card content. When I hover my mouse over the card, I want the card to slightly slide up.
  - Can you rewrite this code using TailwindCSS?
  - When I click on the button, send an HTTP request to /api/products. Instead of the fetch API, use Axios. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I need the HTML and CSS in separate files for a blog homepage with a navbar with a logo on the left and links on the right. A hero area with a background image and centered text. Under that should be 3 cards in a horizontal flexbox. The cards should have light gray background and a box shadow. Use light blues and greens and use the poppies font. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### React Examples

- Create a React component for displaying a card
  - Deconstruct the props parameter ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Create a basic react component that says hello world. CODE ONLY.
  - Add a button that toggles the visibility of the text.
  - Now write a test for this app using Playwright.
  - Document this code. ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))

#### SQL Examples

- Write an SQL query to generate a table called products with 4 columns ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Write an SQL query to generate a table called products with these columns: Id (int), Title (string), Category (int), unitPrice (float), and imageUrl (string) ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Write an SQL query to retrieve the top 5 customers in Manhattan
  - Revise this query and join the customers table with the orders table to find out how much each customer has spent. Then pick the top 5 who have spent the most. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

![ChatGPT 101](https://doodleipsum.com/700?i=caffe290950cc7d4d508bb5755421d7f)

## ChatGPT's API (For Developers)

[Return to top](#top)

API documentation in the works (requires to pay for ChatGPT)

<!-- ### ChatGPT's API

ChatGPT's API Documentation: <https://platform.openai.com/>

#### [Chat completions](https://platform.openai.com/docs/guides/chat)

NOTE: Only useable for paid versions `gpt-3.5-turbo` and `gpt-4`. -->

![ChatGPT 101](https://doodleipsum.com/700?i=95776567c40a23a5a07a8f0a93add37d)

## Closing Credits

[Return to top](#top)

A special shout-out to [Nick Arocho](https://www.nickarocho.com/) for his initial guidance on where to get started with ChatGPT. Videos by [Traversy](https://www.youtube.com/watch?v=o_joulYVndM), [Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc), [Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw), [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A), and [Beyond Fireship](https://www.youtube.com/watch?v=e2uvhJ7r1UQ). Doodles by [Doodle Ipsum](https://doodleipsum.com/).

---

© 2023 Brady Gerber. All Rights Reserved.

[Return to top](#top)
