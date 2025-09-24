from config import get_connection

class User:
    @staticmethod
    def add_user(name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        conn.close()
        print(f"✅ User '{name}' registered.")

    @staticmethod
    def view_users():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
        conn.close()
