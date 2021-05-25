from SQLAlchemy import Column, String, Integer, Flaot
from base import Base


class Processor(Base):
    __tablename__ = "processor"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cores = Column(Integer)
    speed = Column(Flaot)
    manufacturer = Column(String)
    phone = relationship("phone")

    def __init__(self, name, cores, speed, manufacturer) -> None:
        self.name = name
        self.cores = cores
        self.speed = speed
        self.manufacturer = manufacturer
