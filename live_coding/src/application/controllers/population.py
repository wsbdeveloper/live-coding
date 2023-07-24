from flask import Flask

from live_coding.src.application.controllers.adapters.population_dto import \
    PopulationDTO
from live_coding.src.application.controllers.exceptions.no_class_app import \
    NotClassApp
from live_coding.src.application.services import population


class ControllerPopulationClimate:
    def population_by_climate(self, app, climate):
        try:
            if not isinstance(app, Flask):
                raise NotClassApp("Class for app not class accepted Flask", code=939)
            
            services_population = population.ServicePopulation().get_list_climate_population(climate=climate)
            # dto
            parsed_response = PopulationDTO(domain_data=services_population)
            return parsed_response.to_json_asc()

        except NotClassApp as erro:
            raise erro