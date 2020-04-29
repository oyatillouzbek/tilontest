import time
import telebot
import urllib3
import json
from datetime import datetime
#import degani bu osha requirements.txt fayli ichidagi modullarni import qilib olyapti yani chaqirib olyaptim

TOKEN = "914816327:AAHHJtlSTKl20xz3wRVcNT4F3qiaSlRD1Os" #token joyi
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):

    for i in msg:
        if '@' in i:
            return i
@bot.message_handler(content_types=['video','photo','sticker','document','audio','voice'])
def all(m):
    if m.chat.type == 'private':
        if m.photo:
            fileid = m.photo[1].file_id
        elif m.video:
                fileid = m.video.file_id
        elif m.sticker:
                fileid = m.sticker.file_id
        elif m.document:
                fileid = m.document.file_id
        elif m.audio:
                fileid = m.audio.file_id
        elif m.voice:
                fileid = m.voice.file_id
                e = m.from_user.username
                http = urllib3.PoolManager()
                link = http.request("GET","https://api.pwrtelegram.xyz/bot{}/getFile?file_id={}".format(TOKEN,fileid))
                link1 = link.data
                jdat = json.loads(link1)
                patch = jdat['result']['file_path']
                send = 'https://storage.pwrtelegram.xyz/{}'.format(patch)
                bot.send_message(m.chat.id,'*File Id:*\n{}'.format(fileid),parse_mode='Markdown')
                bot.send_message(m.chat.id,'File Uploaded\nYour link: {}'.format(send))
@bot.message_handler(commands=['start'])
def send_welcome(message):
  sped = "Speeed: "
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
