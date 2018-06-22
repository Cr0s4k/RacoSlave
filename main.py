import telebot
import json
from pprint import pprint
import time
from pyvirtualdisplay import Display
import sys
from scrapper import Scrapper
from configuration import Configuration



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

    @bot.message_handler(commands=['Start'])
    def send_welcome(message):
        global running, last, firstTime

        if not running:
            bot.reply_to(message, "Let's get started!")
            
            running = True
            while(running):
                result = scrapper.getResult()

                if(result != last):
                    last = result
                    if not firstTime: bot.reply_to(message, "New notices!")
                    scrapper.writeResult(result)
                
                if firstTime: firstTime = False

                time.sleep(60 * 30)

    @bot.message_handler(commands=['Stop'])
    def send_finish(message):
        global running
        running = False;
        bot.reply_to(message, "Program has stopped")

    @bot.message_handler(commands=['Show'])
    def send_finish(message):
        global last
        bot.reply_to(message, str(last))

    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        bot.reply_to(message, message.text)


    ## MAIN
    try:
        with open(config["resultFile"], "r") as file:
            global last
            last = json.load(file)
    except:
        last = {}

    bot.polling()