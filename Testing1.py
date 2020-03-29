# This is the draft written using Sublime Text, same as the one found in the Jupyter Notebook 
# This is my first try, still very new to using Python and building bots

import telegram
import logging

from telegram.ext import Updater, CommandHandler, Message Handler, Filters

# token value refers to the API token of your bot
bot = telegram.Bot(token='1047383488:AAHJVUq0okWEBoPktfnR68bkE96mRcrTysA')

# to test whether your bot is running. Insert your bot display name and username 
print(bot.get_me()) {"first_name": "TrainingBot", "username": "tbica19_bot"}

updater = Updater(token='1047383488:AAHJVUq0okWEBoPktfnR68bkE96mRcrTysA', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# List of Commands for the Bot 
def start(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="I am a bot that tries my best to answer your queries")
start_handler = CommandHandler('start', start) dispatcher.add_handler(start_handler)

def how(update, context):
