from config import get_connection

class Book:
    @staticmethod
    def add_book(title, author):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        conn.commit()
        conn.close()
        print(f"✅ Book '{title}' added.")

    @staticmethod
    def view_books():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            print(row)
        conn.close()
