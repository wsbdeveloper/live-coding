class DataAPI:
    def __init__(self, umidade, temp, atmospheric_press, city, population):
        self._umidade = umidade
        self._temp = temp
        self._atmospheric_press = atmospheric_press
        self._city = city
        self._population = population

    @property
    def umidade(self):
        return self._umidade

    @umidade.setter
    def umidade(self, value):
        self._umidade = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def atmospheric_press(self):
        return self._atmospheric_press

    @atmospheric_press.setter
    def atmospheric_press(self, value):
        self._atmospheric_press = value
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        self._city = value

    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, value):
        self._population = value