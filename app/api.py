from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

import nltk
from nltk.chat.util import Chat, reflections

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://dheeraj07.netlify.app",
    "dheeraj07.netlify.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

pairs = [
    ['hi', ['Hello! I am Selina, a low-key personal assistant developed by Dheeraj. How can I help you today?']],
    ['(.*) you', ['My name is Selina.A chatbot created by Dheeraj']],
    ['(.*) name', ['My name is Selina.A chatbot created by Dheeraj']],['(.*) about', ['He is experienced in web development and related frameworks, and that he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) about', ['He is experienced in web development and related frameworks, and he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) your', ['He is experienced in web development and related frameworks, and he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) Dheeraj', ['He is experienced in web development and related frameworks, and  he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) creator', ['He is experienced in web development and related frameworks, and he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) projects', ['his current projects include a cloud-based blog that uses authentication and data storage in the cloud, and a chatbot for booking a service. He is also working on a project using gesture recognition.']],
    ['(.*) contact', ['You can contact the creator by the profiles given below.']],
    ['(.*)', ['Sorry, I do not understand what you are saying.']]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

@app.get("/chat")
def get(query:str):
    print(query)
    response = chatbot.respond(query)
    return {"response":response}
