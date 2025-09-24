from book import Book
from user import User
from transaction import Transaction
from utils import menu

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        Book.add_book(title, author)

    elif choice == "2":
        Book.view_books()

    elif choice == "3":
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        User.add_user(name, email)

    elif choice == "4":
        User.view_users()

    elif choice == "5":
        user_id = int(input("Enter user ID: "))
        book_id = int(input("Enter book ID: "))
        Transaction.issue_book(user_id, book_id)

    elif choice == "6":
        transaction_id = int(input("Enter transaction ID: "))
        Transaction.return_book(transaction_id)

    elif choice == "7":
        print("👋 Exiting system.")
        break
    else:
        print("❌ Invalid choice.")
