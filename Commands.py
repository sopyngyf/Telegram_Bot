# List of Commands for the Bot when you type /cmd to the bot
# Still very new to Python

from telegram.ext import Updater
from telegram import InilneKeyboardButton, InlineKeyboardMarkup
from telegram.utils.helpers import escapt_html, escape_markdown
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser