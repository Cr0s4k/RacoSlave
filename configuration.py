import json

class Configuration:
    def read_configuration():
        with open('configuration.json') as f:
            data = json.load(f)
            return data