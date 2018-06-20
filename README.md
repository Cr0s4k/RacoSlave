# RacoSlave
RacoSlave is a script that notifies you (sending you a message through a telegram bot) when there is a new notice in one of your subjects.
It works by scrapping 
[**el Racó**](https://raco.fib.upc.edu/home/portada/omar.anibal.garcia) and that is why it is necessary to have an account and furthermore you need to have a [telegram bot token](https://core.telegram.org/bots#6-botfather).

## Usage: 

- Install libreries 

    ```pip3 install -r requirements.txt```

- Download chrome driver from [here](http://chromedriver.chromium.org/downloads)

- Rename configuration.copy.json to configuration.json and fill it

    ```mv configuration.copy.json configuration.json```

- Run main.py

    ```python3 main.py```


### About configuration.json
    username: Raco username
    password: Raco password
    botToken: TelegramBotToken
    driverPath: Chrome driver path
    resultFile: Json file where you want to store results obtained with scrapping (Can be invented as result.json)