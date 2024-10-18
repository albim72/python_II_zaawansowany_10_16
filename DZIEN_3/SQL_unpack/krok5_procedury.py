from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ThreadPoolExecutor

# Konfiguracja połączenia do bazy MySQL
DATABASE_URL = 'mysql+pymysql://root:abc123@localhost/zaawansowana_baza'
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)


# Funkcja do wywoływania procedury AddUser
def add_user(name, email):
    with Session() as session:
        session.execute(text("CALL AddUser(:name, :email)"), {'name': name, 'email': email})
        session.commit()


# Funkcja do wywoływania procedury GetUserPosts
def get_user_posts(user_id):
    with Session() as session:
        result = session.execute(text("CALL GetUserPosts(:user_id)"), {'user_id': user_id})
        posts = result.fetchall()
        for post in posts:
            print(post)
        session.commit()


# Równoległe uruchamianie procedur
if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        # Równoczesne dodawanie użytkowników
        futures = [
            executor.submit(add_user, 'Alice', 'alice@example.com'),
            executor.submit(add_user, 'Bob', 'bob@example.com')
        ]

        # Czekamy na zakończenie dodawania użytkowników
        for future in futures:
            future.result()

        # Równoczesne pobieranie postów użytkownika
        post_futures = [
            executor.submit(get_user_posts, 1),  # Pobieranie postów użytkownika o ID 1
            executor.submit(get_user_posts, 2)  # Pobieranie postów użytkownika o ID 2
        ]

        # Czekamy na zakończenie pobierania postów
        for future in post_futures:
            future.result()
