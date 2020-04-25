import time
import telebot
import pyspeedtest
from datetime import datetime
#import degani bu osha requirements.txt fayli ichidagi modullarni import qilib olyapti yani chaqirib olyaptim

TOKEN = "token joyi" #token joyi
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):

    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start'])
def send_welcome(message):
  sped = "Tezlik: "
  start = datetime.now()
  msge = bot.reply_to(message, sped)
  end = datetime.now()
  ms = (end - start).microseconds / 1000
  speed = sped + str(ms)
  bot.edit_message_text(speed,chat_id=msge.chat.id, message_id=msge.message_id)

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)

def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': 
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)
        
    
bot.polling(none_stop=True) #biu doimo kod oxirida huddi shunday turishi kerak.