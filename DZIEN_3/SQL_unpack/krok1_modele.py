from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Konfiguracja połączenia do MySQL
DATABASE_URL = 'mysql+pymysql://root:abc123@localhost/zaawansowana_baza'
engine = create_engine(DATABASE_URL, echo=True)

# Deklaratywna baza
Base = declarative_base()


# Model użytkownika
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

    # Relacja jeden do wielu
    posts = relationship('Post', back_populates='user')


# Model postu (blogu, artykułu itp.)
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Powiązanie z użytkownikiem
    user = relationship('User', back_populates='posts')


# Tworzenie tabel
Base.metadata.create_all(engine)
