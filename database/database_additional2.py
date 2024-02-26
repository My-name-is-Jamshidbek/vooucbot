import sqlite3
from config import DATABASE_NAME

def create_inviters_table():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    # Create the user table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS inviters
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 offerer TEXT NOT NULL,
                 offered TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def add_inviter_user(offerer, offered):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("INSERT INTO inviters (offerer, offered) VALUES (?, ?)", (offerer, offered))

    conn.commit()
    conn.close()

def get_offerer_user(offered):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    # Assuming you have a table named 'inviters' with columns 'offerer' and 'offered'
    c.execute("SELECT offerer FROM inviters WHERE offered = ?", (offered,))
    result = c.fetchone()

    conn.close()

    if result:
        # If a record is found, return the offerer
        return result[0]
    else:
        # If no record is found, return False
        return False
