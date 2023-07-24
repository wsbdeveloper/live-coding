import json


class DataAPI:
    def __init__(self, umidade, temp, atmospheric_press, city, population):
        self.umidade = umidade
        self.temp = temp
        self.atmospheric_press = atmospheric_press
        self.city = city
        self.population = population

    def to_json(self):
        return json.dumps(self)