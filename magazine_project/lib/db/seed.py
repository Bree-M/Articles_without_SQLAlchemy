from lib.db.connection import get_connection

seed_data = [
    ("Alice"),
    ("Bob")
]

def seed():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors")
    for name in seed_data:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
    print("Seeded database successfully")