from SQLAlchemy import create_engine
from SQLAlchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///database.sqlite', echo=True)

session = sessionmaker(bind=engine)

Base = declarative_base()
