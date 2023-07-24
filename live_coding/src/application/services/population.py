from typing import List

from live_coding.src.application.use_cases.population_climate import \
    PopulationClimateImp
from live_coding.src.domain.data_brazil import DataAPI
from live_coding.src.infra.databases.migrations.conn import session_orm
from live_coding.src.infra.databases.migrations.models.simulation_population import \
    ConsultPopulation


class ServicePopulation:
    """
        Service - Classes de integrações / comunicações externas / use cases
    """
    
    def get_list_climate_population(self, climate) -> List[DataAPI]:
        use_case_population = PopulationClimateImp()
        data = use_case_population.consulting_climate(climate=climate)
        print("oioi")
        breakpoint()
        print("oioi")
        
        if data is None: 
            return []
        
        # try raise saved is not success!
        for population in data:
            new_consult = ConsultPopulation(temp=population.temp, city=population.city, population=population.population)
            session_orm.add(new_consult)
            session_orm.commit()

        return data
