import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)


def init(force: bool = False):
    c = conn.cursor()
    if force:
        c.execute("DROP TABLE IF EXISTS users")

    c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id         INT     PRIMARY KEY NOT NULL,
                user_name       TEXT    NOT NULL,
                user_weight     FLOAT,
                user_height     INT)
            """)
    conn.commit()
    c.close()


def add_new_user(user_id: int, full_name: str, weight: float, height: int):
    c = conn.cursor()
    c.execute("INSERT INTO users (user_id, user_name, user_weight, user_height) VALUES (?, ?, ?, ?)",
              (user_id, full_name, weight, height))
    conn.commit()
    c.close()


def check_user(user_id: int) -> bool:
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id, ))
    selected = c.fetchone()
    c.close()
    if not selected:
        return True
    return False


# def change_user_params(weight: float, height: int):
#     c = conn.cursor()
#     c.close()
