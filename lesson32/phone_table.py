from SQLAlchemy import Column, String, Float, Integer
from base import Base


class Phone(Base):
    __tablename__ = "phone"
    id = Column(Integer,primary_key=True)
    company = Column(String)
    model = Column(String)
    diagonal = Column(Float)
    price = Column(Integer)
    proccesor_id = Column(Integer, ForeignKey('phone.id'))

    def __init__(self, company, model, diagonal, price) -> None:
        self.company = company
        self.model = model
        self.diagonal = diagonal
        self.price = price
