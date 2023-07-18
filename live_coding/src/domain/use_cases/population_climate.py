from abc import ABC, abstractmethod

from live_coding.src.infra.protocols.http import api_climate


class PopulationClimate(ABC):        
    @abstractmethod
    def consulting_climate(self, climate: str):
        """
            Running the consult apis for merged the informations for calculate and
            informations for response in consult by climate.
        """
        pass
