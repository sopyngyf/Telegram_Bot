# List of Commands for the Bot when you type /cmd to the bot
# Still very new to Python

# List of Commands for the Bot when you type /cmd to the bot
def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="I am a bot that tries my best to answer your queries")
start_handler = CommandHandler('start', start) 
dispatcher.add_handler(start_handler)

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
