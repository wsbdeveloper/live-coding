class DataAPI:
    def __init__(self, umidade, temp, atmospheric_press):
        self.umidade = umidade
        self.temp = temp
        self.atmospheric_press = atmospheric_press

    @property
    def umidade(self):
        return self.umidade

    @property.setter
    def umidade(self, value):
        self.umidade = value

    @property
    def temp(self):
        return self.temp

    @property.setter
    def temp(self, value):
        self.temp = value

    @property
    def atmospheric_press(self):
        return self.atmospheric_press

    @property.setter
    def atmospheric_press(self, value):
        self.temp = value