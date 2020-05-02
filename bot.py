from pyrogram import Client, Filters
import asyncio
import os
api_id = 1194939
api_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash)
    

@app.on_message(Filters.new_chat_members)
def newuser(client,message):
    chatidi = str(message.chat.id)
    if not os.path.exists(chatidi):
        os.makedirs(chatidi)
    for i in message.new_chat_members:
        userid = str(i.id)
        fromid = str(message.from_user.id)
    if userid == fromid:
            put = open(chatidi + "/" + userid + ".txt","w")
            put.write("0")
            put.close()
    else:
        if not os.path.exists(chatidi + "/" + fromid + ".txt"):
            put = open(chatidi + "/" + fromid + ".txt","w")
            put.write("0")
            put.close()
        get = open(chatidi + "/" + fromid + ".txt","r")
        get = get.read()
        get = int(get)
        get += 1
        put = open(chatidi + "/" + fromid + ".txt","w")
        put.write(str(get))
        put.close()
        
@app.on_message(Filters.text)
def txt(client,message):
    chatidi = str(message.chat.id)
    if not os.path.exists(chatidi):
        os.makedirs(chatidi)
    if message.chat.type == "supergroup" or message.chat.type == "group":
        if "/get" in message.text and not message.reply_to_message:
            fromid = str(message.from_user.id)
            if not os.path.exists(chatidi + "/" + fromid + ".txt"):
                put = open(chatidi + "/" + fromid + ".txt","w")
                put.write("0")
                put.close()
            get = open(chatidi + "/" + fromid + ".txt","r")
            get = get.read()
            get = str(get)
            message.reply_text("Siz shu kungacha " + get +"ta odam qo'shgansiz.")
        elif "/get" in message.text and message.reply_to_message:
            replyid = str(message.reply_to_message.from_user.id)
            if not os.path.exists(chatidi + "/" + replyid + ".txt"):
                put = open(chatidi + "/" + replyid + ".txt","w")
                put.write("0")
                put.close()
            firstname = str(message.reply_to_message.from_user.first_name)
            MENTION = "[{}](tg://user?id={})"
            get = open(chatidi + "/" + replyid + ".txt","r")
            get = get.read()
            get = str(get)
            text = MENTION.format(firstname,replyid)
            message.reply_text(text +" shu kungacha " + get +"ta odam qo'shgan.")


app.run()
