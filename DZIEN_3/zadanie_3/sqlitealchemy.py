from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = 'sqlite:///mojabaza.db'

#tworzenie połączenia z bazą
engine = create_engine(database_url)

#tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

session.close()
