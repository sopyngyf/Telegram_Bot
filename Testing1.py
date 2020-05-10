# This is the draft written using Sublime Text, same as the one found in the Jupyter Notebook 
# This is my first try, still very new to using Python and building bots

import telegram
import logging
import threading

import config

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

# token value refers to the API token of your bot
bot = telegram.Bot(config.access_token)

# to test whether your bot is running. Insert your bot display name and username 
print(bot.get_me()) 
{"first_name": "TrainingBot", "username": "tbica19_bot"}

updater = Updater(config.access_token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# List of Commands for the Bot when you type /cmd to the bot
def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="I am a bot that tries my best to answer your queries")
start_handler = CommandHandler('start', start) 
dispatcher.add_handler(start_handler)

def shutdown():
	updater.stop()
	updater.is_idle = False

def stop(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="Bot is done for today")
stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)

def how(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="type / followed by keyword, for example, /about")
how_handler = CommandHandler('how', how)
dispatcher.add_handler(how_handler)

def about(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="This is a bot to answer your query")
about_handler = CommandHandler('about', about)
dispatcher.add_handler(about_handler)

def mc(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="Submit MC by the following day deployed at HTA. Apply via the PaC@Gov app also")
mc_handler = CommandHandler('mc', mc)
dispatcher.add_handler(mc_handler)

def dutyphone(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="Training Command Duty Phone number is 9299 2462")
dutyphone_handler = CommandHandler('dutyphone', dutyphone)
dispatcher.add_handler(dutyphone_handler)

#Start Bot
#updater.start_polling()

#Stop Bot
updater.stop()

#End of Code