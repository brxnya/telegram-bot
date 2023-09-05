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
                user_height             INT,
                user_physical_activity  TEXT
                )
            """)
    conn.commit()
    c.close()


def add_new_user(user_id: int, name: str, gender: str, age: int, weight: float, height: int, activity: str):
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
    c.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
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


def change_user_params(user_id: int, gender=None, age=None, weight=None, height=None, activity=None):
    c = conn.cursor()
    if gender:
        c.execute("UPDATE users SET user_gender = ? WHERE user_id = ?", (gender, user_id))
        conn.commit()
    elif age:
        c.execute("UPDATE users SET user_age = ? WHERE user_id = ?", (age, user_id))
        conn.commit()
    elif weight:
        c.execute("UPDATE users SET user_weight = ? WHERE user_id = ?", (weight, user_id))
        conn.commit()
    elif height:
        c.execute("UPDATE users SET user_height = ? WHERE user_id = ?", (height, user_id))
        conn.commit()
    elif activity:
        c.execute("UPDATE users SET user_physical_activity = ? WHERE user_id = ?", (activity, user_id))
        conn.commit()
    c.close()
