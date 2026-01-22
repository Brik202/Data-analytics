import os
import random
import time

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def env(name: str, default: str) -> str:
    v = os.getenv(name)
    return default if v is None or v == "" else v


db_config = {
    "dbname": env("dbName", "game"),
    "user": env("dbUser", "game"),
    "password": env("dbPassword", "game"),
    "host": env("dbHost", "localhost"),
    "port": env("dbPort", "5432"),
}

PERIOD_SEC = 1


PLAYERS = [
    "Alisa",
    "Borya",
    "Chuckie",
    "Diana",
    "Eva",
    "Mukhtar",
    "Gosha",
    "Anton",
    "Irina",
    "Jora",
    "Katya",
    "Lev",
]

ACTIONS = [
    "start_level",
    "finish_level",
    "collect_item",
    "defeat_enemy",
    "use_boost",
]


def connect():
    return psycopg2.connect(**db_config)


def gen_event():
    player = random.choice(PLAYERS)
    level = random.randint(1, 60)
    action = random.choice(ACTIONS)

    points_by_action = {
        "start_level": random.randint(0, 5),
        "finish_level": random.randint(50, 200),
        "collect_item": random.randint(5, 25),
        "defeat_enemy": random.randint(20, 120),
        "use_boost": random.randint(1, 15),
    }
    points = int(points_by_action[action] + level * random.uniform(0.1, 0.8))

    return player, action, points, level


def insert_event(cur, row):
    cur.execute(
        'INSERT INTO "События" ("игрок", "действие", "очки", "уровень") VALUES (%s, %s, %s, %s);',
        row,
    )


def main():
    while True:
        try:
            conn = connect()
            conn.autocommit = True
            cur = conn.cursor()

            row = gen_event()
            insert_event(cur, row)

            print(f"player={row[0]} action={row[1]} points={row[2]} level={row[3]}")

            cur.close()
            conn.close()
        except psycopg2.Error as e:
            print(f"Ошибка при работе с БД: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            time.sleep(2)

        time.sleep(PERIOD_SEC)


if __name__ == "__main__":
    main()
