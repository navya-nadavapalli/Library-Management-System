 # 📚 Library Management System (Python + MySQL)

A simple Library Management System built using **Python** and **MySQL**.

## 🚀 Features
- Add and view books
- Register and view users
- Issue and return books
- Tracks book availability

## 🛠 Tech Stack
- Python
- MySQL
- mysql-connector-python

## ⚙️ Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/Library-Management-System.git
   cd Library-Management-System
2. Install dependencies:  
pip install -r requirements.txt
3. Import database:
mysql -u root -p < database.sql
4. Run the app:
python main.py


## Sample Usage
1. Add User  
   Input: `Navya, navya@example.com`  
   Output: ✅ User 'Navya' registered.

2. Add Book  
   Input: `Python Programming, John Doe`  
   Output: ✅ Book added.

3. Issue Book  
   Input: `User ID: 1, Book ID: 1`  
   Output: 📚 Book issued successfully.


