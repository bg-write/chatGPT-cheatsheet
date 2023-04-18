<a name="top"></a>

# ChatGPT, AI & Machine Learning: How to Get Started (and Not Be Afraid)

[![GitHub issues](https://img.shields.io/github/issues/bg-write/chatGPT-cheatsheet?style=flat-square)](https://github.com/bg-write/chatGPT-cheatsheet/issues)

![ChatGPT 101](https://doodleipsum.com/700/flat?i=dc8797cdd78c30bd8c72a5fbf1157b7e)

## Table of Contents

- Getting Started (Who is This Guide For?)
- AI Overview
- Machine Learning Overview
- ChatGPT Overview
- Getting Started With ChatGPT (On Your Computer)
- ChatGPT For Newbies
- ChatGPT's API (For Developers)
- Closing Credits

---

## Getting Started (Who is This Guide For?)

[Return to top](#top)

### ChatGPT Explained in One Sentence (to a Newbie)

ChatGPT is a computer grogram that can understand and generate human-like language to have conversations with people.

(NOTE: This is the answer I got when I asked ChatGPT to explain itself in one sentence to someone who knows nothing about ChatGPT or AI.)

### ChatGPT Explained in One Sentence (to an Experienced Engineer)

ChatGPT is a state-of-the-art, large-scale natural language processing model based on the Transformer architecture, which can generate human-like text and perform various language-related tasks with high accuracy.

(This time, I asked ChatGPT to sum itself up in one sentence to an expert. Pretty cool, right?)

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

Another thing I remind myself when it comes to new tools that make my coding life easier: being a great developer means being a great problem solver. The users who will get the most out of ChatGPT are the ones most interested in solving problems and asking smart and informed questions. This is also an opportunity to develop your skills as a problem solver and think of more thoughtful and creative questions to think about when approaching problems.

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

### Metaphors to Help Visualize What ChatGPT Can (and Can't) Do

- **ChatGPT is like a very tech-savvy intern**. It's helpful when assisting you in work that you can do on your own but might be too repetitive or time-consuming. If you feel comfortable handing off work to ChatGPT that you can also fact-check on your own, you're in good hands.
- If the Internet is like a sacred text, **ChatGPT is like a rabbi, mullah, or priest of the information found on the Internet**. ChatGPT interprets and conveys information available on the Internet in a way that's easy to read and digest. This communication can help visualize and break-down ideas, but they should be taken with a grain of salt and should not be a substitute for your own knowledge.
- **ChatGPT is like a very knowledgeable person**. This is not the same thing as being a very smart person, or a wise person. ChatGPT's access to information is impressive, but dumb questions will not always yield smart answers; ChatGPT will not be able to always figure out the intent or context of your questions unless you explicitly tell it. This is where the famous expression "garbage in, garbage out" comes into play.

---

### ChatGPT Prompt Categories & Examples to Get You Started (with Sources)

#### General Learning, Troubleshooting, Or Brainstorming

- What are the top 3 books for learning Java? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- What are the key takeaways from BOOK? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- What does WORD mean?
  - Now give me a synonym.
  - Now use it in 10 sentences. ([Santrel](https://youtu.be/jHv63Uvk5VA))
- How do I become a front-end developer? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I want to hire a graphic designer to design my website. We've agreed that they will deliver the first draft in two weeks and offer three iterations free of charge. Any iteration after will be charged at $50/hour. Write a contract for us. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc)) (Obviously run any contracts you'll actually use by a real-life lawyer first.)
- Write an email to my boss asking for a raise. I've worked at this company for 2 years and successfully delivered several projects on time. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I want to learn about the fetch API. What are the steps that I should take?
  - Tell me more about #2.
  - Show me an example of the fetch API and a POST request.
  - Show me this example using async await.
  - What are some good books about the fetch API?
  - What about YouTube videos? ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))
- Give me some ideas for an app that uses the geolocation API.
  - Tell me more about #3. ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Creating Your Own Study Guide

- Give me a study plan to learn Python for data science with resources and a timeline. ([Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs))
- Act as a coding tutor that creates study plans to help people learn to code. You will be provided with the goal of the student, their time commitment, and resource preferences. You will create a study plan with timelines and links to resources. Only include relevant resources because time is limited. My first request: "I want to become a data scientist but I do not know how to code. I can study 10 hours per week and only want video resources. I want to learn to code in Python. Create a study plan for me." ([Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs))

#### Generating Project Ideas

- Act as an expert data scientist and create an exploratory data analysis Python data science project about Naruto the anime. ([Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs))

#### Preparing For A Job Interview

- I have three years of experience coding in HTML, CSS, and JavaScript. Write a resume for me. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- I'm applying for a front-end engineer role at COMPANY. Write a cover letter for me. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Act as a technical interviewer and ask me 5 questions about JavaScript
  - What is the answer to the first question? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- You are conducting an interview for a senior Front End developer role. I want you to ask me difficult React.js, HTML, CSS, and JavaScript interview questions. Your response should contain the difficulty rating, but do not give me the answer or any other information. Start by asking me one question. ([Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw))
- Can you give me an HTML question about accessibility? ([Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw))
- Explain JavaScript like I'm a 5-year-old. ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))
- What are the three most important concepts to know in React.js? ([Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A))

#### Working In Excel

- Write an Excel formula to add up values in cells B2 through B10.
  - Can you explain how this function works? ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to calculate the profit. The revenue is in cell A2 and the cost is in B2. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to find "Sugar Cookie" in a table and return the price.
  - Can I use any other functions? ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to extract all the text before the @ character in cell A2. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel formula to count the number of unique values in a list. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))
- Write an Excel macro to send emails. Use the following subject: "Kevin Cookie Company Invoice." Use the following text: "You owe the Kevin Cookie Company X." Take the value X from column A. Send it to the email address listed in column B. ([Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s))

#### Writing Shell (Linux) Commands

- Write a bash command to find the name of all jpeg files in a directory and write them all to a text file. ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

#### Writing Git Commands

- How do I know how many lines of code I've committed to a Git repository? ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))

#### Improving Code & Getting Feedback

- How can I improve this code? [Then paste code.] ([Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc))
- Can you provide some feedback on this code (then paste the code). ([Traversy](https://www.youtube.com/watch?v=o_joulYVndM))

#### Extracting Data

- Based on this Wikipedia article, when was the first Model T made? [paste in the article text or wiki url]
  -Now output that as a Python variable. ([Santrel](https://youtu.be/jHv63Uvk5VA))

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

#### Building An API

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

ChatGPT's Overall API Documentation: <https://platform.openai.com/>

OpenAI's Playground (to test out completions): <https://platform.openai.com/playground>

ChatGPT API library (Python): <https://platform.openai.com/docs/libraries/python-bindings>

ChatGPT API library (Node.js): <https://platform.openai.com/docs/libraries/node-js-library>

ChatGPT API Community libraries (multiple languages): <https://platform.openai.com/docs/libraries/community-libraries>

ChatGPT API Application Examples: <https://platform.openai.com/examples>

![ChatGPT 101](https://doodleipsum.com/700?i=95776567c40a23a5a07a8f0a93add37d)

## Closing Credits

[Return to top](#top)

A special shout-out to [Nick Arocho](https://www.nickarocho.com/) for his initial guidance on where to get started with ChatGPT.

Cited videos by:

- [Traversy](https://www.youtube.com/watch?v=o_joulYVndM)
- [Mosh](https://www.youtube.com/watch?v=sTeoEFzVNSc)
- [Kevin Stratvert](https://www.youtube.com/watch?v=JYtZ2zsdE_s)
- [Santrel](https://youtu.be/jHv63Uvk5VA)
- [Tina Huang](https://www.youtube.com/watch?v=VznoKyh6AXs)
- [Web Dev Simplified](https://www.youtube.com/watch?v=Btc9sRIu2jw)
- [Fireship](https://www.youtube.com/watch?v=iO1mwxPNP5A)
- [Beyond Fireship](https://www.youtube.com/watch?v=e2uvhJ7r1UQ)

Doodles by [Doodle Ipsum](https://doodleipsum.com/).

---

© 2023 Brady Gerber. All Rights Reserved.

[Return to top](#top)
