class APIkeys:

    def __init__(self):
        with open('config.txt') as file:
            lines = file.read().splitlines()
            for line in lines:
                split_line = line.split('=', 1)
                if split_line[0] == 'weather_key':
                    self.weather_key = split_line[1]
                elif split_line[0] == 'translator_key':
                    self.translator_key = split_line[1]
                elif split_line[0] == 'events_key':
                    self.events_key = split_line[1]

    def get_weather_key(self):
        return self.weather_key

    def get_translator_key(self):
        return self.translator_key

    def get_events_key(self):
        return self.events_key


if __name__ == '__main__':
    api_key = APIkeys()
    print(api_key.get_weather_key())
    print(api_key.get_events_key())
    print(api_key.get_translator_key())
