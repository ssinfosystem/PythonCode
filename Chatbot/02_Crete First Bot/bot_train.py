from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():

    chatbot = ChatBot("Cheru")

    # Conversion Flow along with Answer
    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome."
    ]

    # Train the Bot
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)

    # Get the Response from Bot
    for file in os.listdir('data'):
            convData = open(r'data/' + file,encoding='latin-1').readlines()
            chatbot.set_trainer(ListTrainer)
            chatbot.train(convData)
            #print("Training completed")

setup()