import random
import sys

from faker import Faker

from app import app, db, Inventory

faker = Faker()

games = [
    "Mictlan Souls",
    "Pixel Raiders",
    "Neon Requiem",
    "Ashes of Tlaloc",
    "Void Hunters",
    "Echo Protocol"
]

genres = [
    "RPG",
    "Souls-like",
    "Terror",
    "Roguelike",
    "Acción"
]

platforms = [
    "PC",
    "Linux",
    "Steam Deck"
]

def create_fake_games(n):

    for i in range(n):

        game = Inventory(

            cliente=faker.user_name(),

            videojuego=random.choice(games),

            genero=random.choice(genres),

            plataforma=random.choice(platforms),

            precio=f"${random.randint(100, 999)}"

        )

        db.session.add(game)

    db.session.commit()

    print(f"{n} registros agregados")

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print("Indica cantidad")
        sys.exit(1)

    with app.app_context():
        create_fake_games(int(sys.argv[1]))
