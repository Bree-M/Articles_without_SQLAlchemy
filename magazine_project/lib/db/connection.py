def get_connection():
    import sqlite3
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory of connection.py
    db_path = os.path.join(base_dir, 'database.db')         # correctly resolves to lib/db/database.db
    return sqlite3.connect(db_path)  # ✅ USE THIS VARIABLE
