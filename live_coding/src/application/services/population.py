from live_coding.src.application.use_cases.population_climate import \
    PopulationClimateImp


class ServicePopulation:
    """
        Service - Classes de integrações / comunicações externas / use cases
    """
    
    def get_list_climate_population(self, climate):
        use_case_population = PopulationClimateImp()
        use_case_population.consulting_climate(climate=climate)