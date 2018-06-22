import telebot
import json
from pprint import pprint
import time
from pyvirtualdisplay import Display
import sys
from scrapper import Scrapper
from configuration import Configuration

def format_result(res):
    out = ""
    for obj in res:
        out += "*" + obj["subject"] + "*" + "\n"
        for notice in obj["notices"]:
            out += "*-* " + notice + "\n"
        out += "\n"
    
    return "0 notices from 0 subjects" if out == "" else out

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--vdisplay":
        display = Display(visible=0, size=(50, 50))
        display.start()

    scrapper = Scrapper()
    config = Configuration.read_configuration()
    token = config["botToken"]
    bot = telebot.TeleBot(token)
    running = False
    firstTime = True
    last = []
    last_update = "Never"

    @bot.message_handler(commands=['Start'])
    def send_welcome(message):
        global running, last, firstTime, last_update

        if not running:
            bot.reply_to(message, "Let's get started!")
            
            running = True
            while(running):
                result = scrapper.getResult()

                if(result != last):
                    last_update = time.strftime('%Y-%m-%d %H:%M:%S')
                    last = result
                    if not firstTime: bot.reply_to(message, "New notices!")
                
                if firstTime: firstTime = False

                time.sleep(config["timer"] * 60)

    @bot.message_handler(commands=['Stop'])
    def send_finish(message):
        global running
        running = False;
        bot.reply_to(message, "Program has stopped")

    @bot.message_handler(commands=['Show'])
    def send_finish(message):
        global last
        last_formated = format_result(last)
        bot.send_message(message.chat.id, last_formated, parse_mode= "MARKDOWN")

    @bot.message_handler(commands=['Info'])
    def send_finish(message):
        global last_update
        out = "*Last update*: " + str(last_update)
        bot.send_message(message.chat.id, out, parse_mode= "MARKDOWN")

    @bot.message_handler(commands=['Commands'])
    def send_finish(message):
        out = "*/Start*: Start program \n"
        out += "*/Stop*: Stop program \n"
        out += "*/Show*: Show all subjects with their notices \n" 
        out += "*/Info*: Get program info such as last update time \n"
        out += "*/Commands*: Get commands and their description \n"   
        bot.send_message(message.chat.id, out, parse_mode= "MARKDOWN")

    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.polling()