from chatterbot import CHatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('lopiruz')
trainer=ListTrainer(bot)

for files in os.listdir('./lopiruz)'): 
    data=open('./lopiruz/'+files,'r').readlines()
 trainer.train(data)
    trainer.train(data)
    trainer.train(data)

