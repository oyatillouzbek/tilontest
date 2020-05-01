from pyrogram import Client, Filters
import asyncio
import os
api_id = 1194939
api_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash)
    
RUNNING = "**Eval Expression:**\n```{}```\n**Running...**"
ERROR = "**Eval Expression:**\n```{}```\n**Error:**\n```{}```"
SUCCESS = "**Eval Expression:**\n```{}```\n**Success**"
RESULT = "**Eval Expression:**\n```{}```\n**Result:**\n```{}```"

@app.on_message(Filters.command("eval", "!"))
def eval_expression(client, message):
    expression = " ".join(message.command[1:])

    if expression:
        m = message.reply(RUNNING.format(expression))

        try:
            result = eval(expression)
        except Exception as error:
            client.edit_message_text(
                m.chat.id,
                m.message_id,
                ERROR.format(expression, error)
            )
        else:
            if result is None:
                client.edit_message_text(
                    m.chat.id,
                    m.message_id,
                    SUCCESS.format(expression)
                )
            else:
                client.edit_message_text(
                    m.chat.id,
                    m.message_id,
                    RESULT.format(expression, result)
                )
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
    if "/get" in message.text and not message.reply_to_message:
        fromid = str(message.from_user.id)
        ssrid = str(message.reply_to_message.from_user.id)
        if not os.path.exists(chatidi + "/" + fromid + ".txt"):
            put = open(chatidi + "/" + fromid + ".txt","w")
            put.write("0")
            put.close()
        get = open(chatidi + "/" + fromid + ".txt","r")
        get = get.read()
        get = str(get)
        message.reply_text("Siz shu kungacha " + get +"ta odam qo'shgansiz.")
    else:
        if not os.path.exists(chatidi + "/" + ssrid + ".txt"):
            put = open(chatidi + "/" + ssrid + ".txt","w")
            put.write("0")
            put.close()
        firstname = str(message.reply_to_message.from_user.first_name)
        MENTION = "[{}](tg://user?id={})"
        fromi = str(message.reply_to_message.from_user.id)
        get = open(chatidi + "/" + fromi + ".txt","r")
        get = get.read()
        get = str(get)
        text = MENTION.format(firstname,fromi)
        message.reply_text(text +" shu kungacha " + get +"ta odam qo'shgan.")


app.run()
