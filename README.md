## Inspiration
The project originated from a discussion about life regrets - what we should have done differently, and if we could travel back in time, what we would tell our past self. Each person's life is shaped by their own unique experiences, and each one of us is exposed to different general knowledge. If only there is a way to compile all the general knowledge across humanity and have that be the guidance of our future steps.

## What it does
Sea of Knowledge is a website that compiles user knowledge - aka “droplets” and arranges them in a map of relevance of drops to one another. When the user views a droplet, they have the option to view another droplet from a list of a few related droplets. Through this, the user can amass a great amount of knowledge by “swimming” through a “stream” of droplets. Users can also contribute droplets to the website and participate in improving Sea of Knowledge by identifying connections between different droplets. This way, the connections between the droplets are better defined, improving the user experience of the application.

## How we built it
We used Python to code our backend with Flask to set up the framework of our application and MongoDB to store our information, as well as HTML and CSS to display our frontend. Our setup is fairly simple for a web application, but as a consequence our setup is serverless: we don’t have a “middleman” with our application, so our client communicates directly with the backend. This is fine for a small audience of well-intentioned users, but if we made plans to expand the project, we would need to remedy this to account for potential malicious individuals.

## Challenges we ran into
Our first issue was an issue that our project aims to solve: a lack of surface level knowledge about a topic. One of our group members hadn’t used Github before and had no knowledge of the different commands. With help from the other two members, she was quickly able to understand the different commands, and we were all on the same level of understanding and could commence coding. However, this brings an important issue to light: there aren’t always people around that you can ask for help. This is a problem Sea of Knowledge aims to solve by providing answers to these questions so that you know what you need in order to do a deep dive into a topic.

We had little success using either psql on a locally hosted database or Google Cloud database. Trying to get these methods to work took up almost half of the hacking time. However, after we switched to MongoDB, which we were more familiar with and had used before, the journey got much smoother.

We also had troubles with debugging. It seemed like whenever we fixed one bug, two more popped up that needed to be fixed. However, with tenacity and lots of Google searches, we crushed our infestation.

## Accomplishments that we're proud of
One of our biggest accomplishments was actually just getting our code to run. Once we decided on a project idea, the rest of Friday night was dedicated to getting our Flask template to work. Even when it did work, we had issues with adding additional pages and getting imports to act like they were supposed to. Our code simply working as it’s meant to is a testament to our group’s determination in the face of adversity.

We’re also proud of our use of MongoDB in our project. We’re able to have users add to our database and see their contributions in real time, which greatly improves the functionality of our website.

## What we learned
Some of the things that we learned are obvious: improved coding skills, knowledge of different coding resources, and the ability to build a project from scratch within the course of just over a day and a half. However, other skills are less obvious: we also learned about the possible long-term impacts of COVID-19 through our project considerations, how to find relevant answers to problems we face, and various mathematical concepts from our illustrations of the connections between our droplets for our project.

## What's next for Sea of Knowledge
If we make plans to expand Sea of Knowledge, our first step would probably be to set up a server to protect our information. We could also work on a more complex interface and additional functionality to improve the user experience.
