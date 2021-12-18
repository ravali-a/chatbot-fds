from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os

def setup():
    chatbot = ChatBot("BPDC Bot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    trainer = ListTrainer(chatbot)
    dirname ='C:/Users/User/Desktop/BPDC_ChatBot/datasets'
    for files in os.listdir(dirname):
        with open(os.path.join(dirname, files), mode = "rt", encoding='latin-1') as f:
            data = f.readlines()
            trainer.train(data)

setup()
