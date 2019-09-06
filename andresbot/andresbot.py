from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
def chatraining():
   bot=ChatBot('andresbot')
   trainer=ListTrainer(bot)

   for files in os.listdir('./andresbot/'): 
      data=open('./andresbot/'+files,'r').readlines()
      trainer.train(data)
      trainer.train(data)
      trainer.train(data)

#------------------------------------------------------------
#------------------------------------------------------------
#chat feature
   while True:
      message=input('\t\t\tYou:')
      if message.strip()!='Bye' or 'bye':
         reply=bot.get_response(message)
         print('lopiruz:',reply)
      if message.strip()=='Bye':
         print('lopiruz:Bye')
         break

chatraining()
