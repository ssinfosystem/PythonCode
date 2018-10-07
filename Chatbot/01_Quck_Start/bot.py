from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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

response = chatbot.get_response("Good morning!")
print(response)


