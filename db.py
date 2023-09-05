import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)


def init(force: bool = False):
    c = conn.cursor()
    if force:
        c.execute("DROP TABLE IF EXISTS users")

    c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id                 INT     PRIMARY KEY NOT NULL,
                user_name               TEXT    NOT NULL,
                user_gender             TEXT,
                user_age                INT,
                user_weight             FLOAT,
                user_height             FLOAT,
                user_physical_activity  TEXT
                )
            """)
    conn.commit()
    c.close()


def add_new_user(user_id: int, name: str, gender: str, age: int, weight: float, height: float, activity: str):
    c = conn.cursor()
    c.execute("""
            INSERT INTO users
            (user_id, user_name, user_gender, user_age, user_weight, user_height, user_physical_activity)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, name, gender, age, weight, height, activity))
    conn.commit()
    c.close()


def check_new_user(user_id: int) -> bool:
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id, ))
    selected = c.fetchone()
    c.close()
    if not selected:
        return True
    return False


def get_user_params(user_id: int) -> tuple:
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    c.close()
    return result


def change_user_params(user_id: int, weight=None, height=None):
    c = conn.cursor()
    if weight:
        c.execute("UPDATE users SET user_weight = ? WHERE user_id = ?", (weight, user_id))
        conn.commit()
    elif height:
        c.execute("UPDATE users SET user_height = ? WHERE user_id = ?", (height, user_id))
        conn.commit()
    c.close()
