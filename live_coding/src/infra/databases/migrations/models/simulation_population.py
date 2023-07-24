from sqlalchemy import Column, DateTime, Float, Integer, String, func

from live_coding.src.infra.databases.migrations import conn


class ConsultPopulation(conn.Base):
    __tablename__ = 'consults_populations_climate'

    def __init__(self, temp, city, population):
        self.temp = temp
        self.city = city
        self.population = population

    
    id = Column(Integer, primary_key=True, autoincrement=True)
    temp = Column(String, nullable=True)
    city = Column(String, nullable=True)
    population = Column(Float, nullable=False)
    created_at = Column("created_at", DateTime,default=func.now(), onupdate=func.now())
    updated_at = Column("updated_at", DateTime,default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<ConsultPopulation(id='{self.id}', climate={self.climate})>"
