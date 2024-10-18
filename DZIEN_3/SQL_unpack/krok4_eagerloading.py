from sqlalchemy.orm import joinedload
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from krok1_modele import User,Post
from krok3_transakcje import Session

# Tworzenie sesji
session = Session()

# Pobranie użytkowników razem z ich postami w jednym zapytaniu
users_with_posts = session.query(User).options(joinedload(User.posts)).all()

for user in users_with_posts:
    print(f"Użytkownik: {user.name}")
    for post in user.posts:
        print(f"  Post: {post.title}")

session.close()
