# RacoSlave
RacoSlave is a script that notifies you (sending you a message through a telegram bot) when there is a new notice in one of your subjects.
It works by scrapping 
[**el Racó**](https://raco.fib.upc.edu/home/portada/omar.anibal.garcia) and that is why it is necessary to have an account and furthermore you need to have a [telegram bot token](https://core.telegram.org/bots#6-botfather).

## Usage: 

- Install libreries

    ```pip3 install -r requirements.txt```

- Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases)

- Install firefox (**If it is not already installed**)

    ```sudo apt-get install firefox```

- Rename configuration.copy.json to configuration.json and fill it

    ```mv configuration.copy.json configuration.json```

- Run main.py

    ```python3 main.py [--vdisplay]```


## About configuration.json
    username: Raco username
    password: Raco password
    botToken: TelegramBotToken
    driverPath: Geckodriver path
    timer: Time in minutes that define when we want to update our subjects/notices

## Bot commands
**/Start** -> Start program

**/Stop** -> Stop program

**/Show** -> Show all subjects with their notices

**/Info** -> Get program info such as last update time

**/Commands** -> Get commands and their description

## How to run in server
In order to run RacoSlave in a server, you need to use virtual display flag or you will get error.
```python3 main.py --vdisplay```