from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():

    chatbot = ChatBot("Cheru")
    # Train the Bot
    chatbot.set_trainer(ListTrainer)
    # Get the Response from Bot
    for file in os.listdir('data'):
            convData = open(r'data/' + file,encoding='latin-1').readlines()
            chatbot.set_trainer(ListTrainer)
            chatbot.train(convData)
            #print("Training completed")

setup()