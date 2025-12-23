from werkzeug.security import generate_password_hash
import sqlite3
def init_staff():
    conn = sqlite3.connect("database.db")
    db = conn.cursor()

    staff_users = [
        ("staff1", "staff123"),
        ("staff2", "staff456"),
        ("staff3", "staff789")
    ]

    for username, password in staff_users:
        password_hash = generate_password_hash(password)
        db.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, 'staff')",
            (username, password_hash)
        )
    print("Staff inserted successfully")
    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_staff()
