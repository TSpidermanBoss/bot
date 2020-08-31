from telegram import ParseMode
from telegram.ext import MessageHandler, Filters, Updater,run_async,CommandHandler
bot = '947124922:AAE955zX-8gNamkfMsAdkzJGveh6On8D8-c'
des = -1001499393629
s = -1001270440497
updater = Updater(token=bot,use_context=True)
@run_async
def send(update,context):
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🥳','link','❓','garr','audio','whatsapp','book','bhai','🐴','only','tennis','teen','line','WICKET LU','?','telegram',"kama","lakh",' id','स']
 for word in words:
  if word.casefold() in update.effective_message.text.casefold():
    return
 mes = context.bot.send_message(des,"*" + update.effective_message.text + "*",parse_mode=ParseMode.MARKDOWN)
 fie = open("ids.txt","a")
 fie.write(" " + str(update.effective_message.message_id) + " " + str(mes.message_id))
 fie.close()
@run_async
def edit(update,context):
   files = open("ids.txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(update.effective_message.message_id)
    if id in x:
      context.bot.edit_message_text("*" + update.effective_message.text + "*",des,int(x[x.index(id)+1]),parse_mode=ParseMode.MARKDOWN)
@run_async
def clear(update,context):
  with open("ids.txt","w") as fie:
   fie.write("001 002")
   fie.close()
   update.message.reply_text("☢️ Done, Editing data cleared ✅✅")
dispatcher = updater.dispatcher
send = MessageHandler(Filters.chat(s) & Filters.text & ~ Filters.update.edited_channel_post ,send)
edit = MessageHandler(Filters.chat(s) & Filters.update.edited_channel_post,edit)
clear = CommandHandler("clear",clear)
dispatcher.add_handler(send)
dispatcher.add_handler(edit)
dispatcher.add_handler(clear)
updater.start_polling()