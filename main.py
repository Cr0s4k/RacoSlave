import telebot
from configuration import Configuration

def getToken():
    with open('credentials.json') as f:
            data = json.load(f)
            return data["botToken"]

config = Configuration.read_configuration()
token = config["token"]
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
        result = subprocess.run(["python3", "lastPost.py"], stdout = subprocess.PIPE)
        #bot.reply_to(message, result.stdout)
        if(result.stdout != last):
            bot.reply_to(message, "NUEVA NOTICIA IDI!")
            last = result.stdout
            file = open("last.txt", "w")
            file.write(str(last))
            file.close()
            #Escribimos
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

file = open("last.txt", "r")
last = file.read()
file.close()

bot.polling()