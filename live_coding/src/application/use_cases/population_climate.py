import json

from live_coding.src.domain.use_cases.population_climate import \
    PopulationClimate
from live_coding.src.infra.protocols.http.api_climate import Apibrazil
from live_coding.src.infra.protocols.http.api_population import ApiIBGE

ID_POPULACAO = 606

class PopulationClimateImp(PopulationClimate):
    def __init__(self) -> None:
        self.citys = []
        self.ibge_population = []
        self.api_climate = []  

    def consulting_climate(self, climate):
        self.api_climate = Apibrazil().get()
        self.population = ApiIBGE().get()
        get_city_data = self.read_json_city()
       
        get_filter_climate = self.filter_climate(data_api_climate=self.api_climate, climate=climate) 
        
        for filter_data in get_filter_climate:
            # consulting citys with climate ps -  (Predomínio de Sol)
            self.find_datasets(data_arr=get_city_data, str_query=filter_data["codigo_icao"])
        
        self.merge(citys=self.citys)

        return self.citys


    def merge(self, citys: list):
        for city in self.citys:
            print(city)
            value = self.filter_population(data_api_ibge=self.population, city_filter=city)

            

    def filter_climate(self, data_api_climate, climate):
        dados_filtrados = [dado for dado in data_api_climate if dado["condicao"] == climate]
        return dados_filtrados
    
    def filter_population(self, data_api_ibge, city_filter):
        # filter population ID
        filtred = self.find_by_id_ibge_response(arr_ibge=data_api_ibge, id=ID_POPULACAO)
        
        series = filtred["resultados"][0]["series"]

        #filter city
        data_filter_city = [city for city in series if city["localidade"]["nome"] == city_filter]
        
        #return data 2010 year
        print(data_filter_city)
        if data_filter_city == []:
            return None 
        return data_filter_city[0]["serie"]["2010"]

    def read_json_city(self):
        with open('live_coding/src/application/data/mapping.json', 'r') as arq_json:
            data = json.load(arq_json)

            return data
    
    def find_datasets(self, data_arr, str_query):
        for item in data_arr['mapping']:
            datasets = item.get('datasets', [])
            if str_query in datasets:
                city = item.get("city")
                if city not in self.citys:
                    self.citys.append(city)
        return self.citys
    
    def find_by_id_ibge_response(self, arr_ibge, id):
        for item in arr_ibge:
            if item["id"] == str(id):
                return item
        return None