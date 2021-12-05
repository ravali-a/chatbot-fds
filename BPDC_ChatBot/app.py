from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatbot import get_response
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

chatbot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(chatbot)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
