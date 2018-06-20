import telebot
from configuration import Configuration
import json
from pprint import pprint
from scrapper import Scrapper

scrapper = Scrapper()
config = Configuration.read_configuration()
token = config["botToken"]
bot = telebot.TeleBot(token)
_continue = True

@bot.message_handler(commands=['Start'])
def send_welcome(message):
    bot.reply_to(message, "Empezemos!")

    import subprocess
    import time
    global _continue, last
    
    _continue = True
    while(_continue):
        result = scrapper.getResult()

        pprint("RESULT")
        pprint(result)

        pprint("LAST")
        pprint(last)

        if(result != last):
            last = result
            bot.reply_to(message, "NUEVA NOTICIA")
            scrapper.writeResult(result)
        else:
            bot.reply_to(message, "No news...")

        time.sleep(10)

@bot.message_handler(commands=['Stop'])
def send_finish(message):
    global _continue
    _continue = False;
    bot.reply_to(message, "El programa ha parado.")

@bot.message_handler(commands=['Show'])
def send_finish(message):
    file = open("last.txt", "r")
    bot.reply_to(message, file.read())
    file.close()

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message, message.text)

try:
    with open(config["resultFile"], "r") as file:
        global last
        last = json.load(file)
except:
    last = {}


bot.polling()