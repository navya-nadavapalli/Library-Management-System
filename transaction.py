from config import get_connection

class Transaction:
    @staticmethod
    def issue_book(user_id, book_id):
        conn = get_connection()
        cursor = conn.cursor()

        # check availability
        cursor.execute("SELECT available FROM books WHERE book_id=%s", (book_id,))
        available = cursor.fetchone()
        if not available or not available[0]:
            print("❌ Book not available.")
            return

        cursor.execute("INSERT INTO transactions (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
        cursor.execute("UPDATE books SET available=FALSE WHERE book_id=%s", (book_id,))
        conn.commit()
        conn.close()
        print("📚 Book issued successfully.")

    @staticmethod
    def return_book(transaction_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT book_id FROM transactions WHERE transaction_id=%s AND return_date IS NULL", (transaction_id,))
        result = cursor.fetchone()
        if not result:
            print("❌ Invalid transaction.")
            return

        book_id = result[0]
        cursor.execute("UPDATE transactions SET return_date=NOW() WHERE transaction_id=%s", (transaction_id,))
        cursor.execute("UPDATE books SET available=TRUE WHERE book_id=%s", (book_id,))
        conn.commit()
        conn.close()
        print("✅ Book returned successfully.")
