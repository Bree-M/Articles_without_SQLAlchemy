from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name.strip()
        self.category = category.strip()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return cursor.fetchall()

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON ar.author_id = a.id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        return cursor.fetchall()

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        return [row[0] for row in cursor.fetchall()]

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, COUNT(ar.id) as article_count FROM authors a
            JOIN articles ar ON ar.author_id = a.id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING article_count > 2
        """, (self.id,))
        return cursor.fetchall()
    
    @classmethod
    def top_publisher(cls):
       conn = get_connection()
       cursor = conn.cursor()
       cursor.execute("""
           SELECT m.*, COUNT(a.id) as article_count
           FROM magazines m
           JOIN articles a ON m.id = a.magazine_id
           GROUP BY m.id
           ORDER BY article_count DESC
           LIMIT 1
    """)
       return cursor.fetchone()

