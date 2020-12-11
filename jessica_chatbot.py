#########jessica_chatbot.py########
'''
https://chatterbot.readthedocs.io/en/stable/quickstart.html#training-your-chatbot
'''
import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Jessica Liang")
trainer = ListTrainer(chatbot)

re_conversation = r'\n\- \- [^\n]+\n'\
+r'(  \- [^\n]+\n)+'

re_sentenece = r'(\- ){1,2}(?P<sentence>[^\n]+)\n'

#parse the conversation data from corpus
conversations = [[t.group('sentence') for t in re.finditer(re_sentenece, c.group())] \
for c in re.finditer(re_conversation, open('corpus.yml').read())]

#train the model
for c in conversations:
	print('training by :\t%s'%(str(c)))
	for i in range(4):
		trainer.train(c)

#test the model
while True:
	text = input()
	response = chatbot.get_response(text)
	print(response)
#########jessica_chatbot.py########
