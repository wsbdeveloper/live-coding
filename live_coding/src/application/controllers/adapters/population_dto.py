# -*- coding: utf-8 -*-

import json
from typing import List

from live_coding.src.domain.data_brazil import DataAPI


class PopulationDTO:
    def __init__(self, domain_data: List[DataAPI]):
        self.data_serialization = []
        self.domain_data = domain_data
    
    def to_json_asc(self):
        population_asc = sorted(self.domain_data, key=lambda data: data.population, reverse=True)
        for cls in population_asc:
            self.data_serialization.append(cls.__dict__)
        
        return json.dumps(self.data_serialization)
    