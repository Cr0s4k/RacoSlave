import json

class Configuration:
    def read_configuration(self):
        with open('credentials.json') as f:
            data = json.load(f)
            return data