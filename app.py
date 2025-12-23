from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "cs50-event-secret"
# secret_key is used to sign session cookies and prevent tampering

def get_db():
    return sqlite3.connect("database.db")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        db.close()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["role"] = user[3]

            if user[3] == "student":
                return redirect("/student")
            else:
                return redirect("/staff")

    return render_template("login.html")
#student registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hash = generate_password_hash(password)

        db = get_db()
        db.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, 'student')",
            (username, hash)
        )
        db.commit()
        db.close()

        return redirect("/")

    return render_template("register.html")
#student dashboard

@app.route("/student")
def student_dashboard():
    if session.get("role") != "student":
        return redirect("/")

    user_id = session.get("user_id")

    db = get_db()
    events = db.execute("SELECT * FROM events").fetchall()
    registered = db.execute(
        "SELECT event_id FROM registrations WHERE user_id = ?",
        (user_id,)
    ).fetchall()
    db.close()

    registered_ids = [r[0] for r in registered]

    return render_template(
        "student_dashboard.html",
        events=events,
        registered_ids=registered_ids
    )

#registering for an event
@app.route("/register_event/<int:event_id>")
def register_event(event_id):
    user_id = session["user_id"]

    db = get_db()
    db.execute(
        "INSERT INTO registrations (user_id, event_id) VALUES (?, ?)",
        (user_id, event_id)
    )
    db.commit()
    db.close()

    return redirect("/student")

#staff dashboard
@app.route("/staff")
def staff_dashboard():
    staff_id = session["user_id"]

    db = get_db()
    events = db.execute(
        "SELECT * FROM events WHERE created_by = ?",
        (staff_id,)
    ).fetchall()
    db.close()

    return render_template("staff_dashboard.html", events=events)
#routing to events
@app.route("/events")
def all_events():
    if session.get("role") != "student":
        return redirect("/")

    user_id = session.get("user_id")

    db = get_db()
    events = db.execute("SELECT * FROM events").fetchall()
    registered = db.execute(
        "SELECT event_id FROM registrations WHERE user_id = ?",
        (user_id,)
    ).fetchall()
    db.close()

    registered_ids = [r[0] for r in registered]

    return render_template(
        "events.html",
        events=events,
        registered_ids=registered_ids
    )

#create event
@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    if session.get("role") != "staff":
        return redirect("/")
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        date = request.form.get("date")

        db = get_db()
        db.execute(
            "INSERT INTO events (title, description, date, created_by) VALUES (?, ?, ?, ?)",
            (title, description, date, session["user_id"])
        )
        db.commit()
        db.close()

        return redirect("/staff")

    return render_template("create_event.html")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

