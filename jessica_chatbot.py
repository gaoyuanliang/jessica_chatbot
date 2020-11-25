#########jessica_chatbot.py########
'''
https://chatterbot.readthedocs.io/en/stable/quickstart.html#training-your-chatbot
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Jessica Liang")

trainer = ChatterBotCorpusTrainer(chatbot)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)
#########jessica_chatbot.py########
