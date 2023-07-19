from live_coding.src.application.use_cases.population_climate import \
    PopulationClimateImp

if __name__ == "__main__":
   cls_population = PopulationClimateImp()
   result = cls_population.consulting_climate(climate="ps")
   print(result)
