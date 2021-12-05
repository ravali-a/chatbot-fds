from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def get_response(usrText):
    chatbot = ChatBot('BPDC Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response':'Could you please rephrase?',
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            'response_selection_method': 'chatterbot.response_selection.get_first_response'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    trainer = ListTrainer(chatbot)

    while True:
        if usrText.strip() != 'Bye':
            result = chatbot.get_response(usrText)
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye!')
            break
