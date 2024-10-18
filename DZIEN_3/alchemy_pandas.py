from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Definiowanie bazy modelowej
Base = declarative_base()

# Definiowanie przykładowej tabeli (modelu ORM)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Tworzenie silnika (np. SQLite w tym przypadku)
engine = create_engine('sqlite:///example.db')

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# Tworzenie sesji do komunikacji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()

# Dodanie przykładowych danych do tabeli
# session.add_all([
#     User(name="Jan", age=30),
#     User(name="Anna", age=25),
#     User(name="Tomek", age=35)
# ])
# session.commit()

# Pobieranie danych z bazy za pomocą SQLAlchemy
users = session.query(User).all()

# Konwersja wyników zapytania do Pandas DataFrame
data = [{'id': user.id, 'name': user.name, 'age': user.age} for user in users]
df = pd.DataFrame(data)

# Wyświetlenie DataFrame
print(df)

# Zamykanie sesji
session.close()
