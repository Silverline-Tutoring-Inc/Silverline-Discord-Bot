from flask import Flask
from threading import Thread
from replit import db

app = Flask('')

@app.route('/')
def home():
    return "EducationalThings Bot Files."

def run():
  app.run(host='0.0.0.0',port=8080)

def online():
    t = Thread(target=run)
    t.start()