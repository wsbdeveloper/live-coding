import json
from typing import List

from live_coding.src.domain.data_brazil import DataAPI
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
        self.list_domain_climate = []

    def consulting_climate(self, climate) -> List[DataAPI]:
        self.api_climate = Apibrazil().get()
        self.population = ApiIBGE().get()
        get_city_data = self.read_json_city()

        # list domain data
        list_data = []
       
        get_filter_climate = self.filter_climate(data_api_climate=self.api_climate, climate=climate) 
        
        for filter_data in get_filter_climate:
            # consulting citys with climate ps -  (Predomínio de Sol)
            city_consult = self.find_datasets(data_arr=get_city_data, str_query=filter_data["codigo_icao"])
            
            if not city_consult == None:
                data_population = self.filter_locale(data_api=self.population, city=city_consult)
                list_data.append(DataAPI(atmospheric_press=filter_data["pressao_atmosferica"], temp=filter_data["temp"], umidade=filter_data["umidade"], city=city_consult, population=data_population[0]["serie"]["2007"]))
        return list_data


    def filter_climate(self, data_api_climate, climate):
        dados_filtrados = [dado for dado in data_api_climate if dado["condicao"] == climate]
        return dados_filtrados
    

    def read_json_city(self):
        with open('live_coding/src/application/data/mapping.json', 'r') as arq_json:
            data = json.load(arq_json)

            return data
    
    def find_datasets(self, data_arr, str_query):
        city_found = ""
        for item in data_arr['mapping']:
            datasets = item.get('datasets', [])
            if str_query in datasets:
                city = item.get("city")
                
                return city
            
        return None
    
    def find_by_id_ibge_response(self, arr_ibge, id):
        for item in arr_ibge:
            if item["id"] == str(id):
                return item
        return None
    
    def filter_locale(self, data_api, city):
        obj_filter = []
        series = data_api[0]["resultados"][0]["series"]

        for serie in series:
            localidade = serie["localidade"]
            if localidade["nome"].lower()  == city.lower():
                obj_filter.append(serie)
        return obj_filter