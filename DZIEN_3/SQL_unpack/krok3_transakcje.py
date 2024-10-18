from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from krok1_modele import User,Post

DATABASE_URL = 'mysql+pymysql://root:abc123@localhost/zaawansowana_baza'
engine = create_engine(DATABASE_URL, echo=True)


# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Tworzenie nowego użytkownika
    new_user = User(name='Jan Kowalski', email='jan.kowalski@example.com')
    session.add(new_user)

    # Tworzenie nowego posta
    new_post = Post(title='Pierwszy post', content='To jest treść pierwszego posta.', user=new_user)
    session.add(new_post)

    # Zapisanie zmian w bazie
    session.commit()

except Exception as e:
    print(f"Błąd: {e}")
    session.rollback()  # Wycofanie zmian w przypadku błędu

finally:
    session.close()
