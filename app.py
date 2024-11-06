from flask import Flask, render_template, redirect, request, url_for, flash, session
from database import db  # Импортиране на db от database.py
from models import User, Task  # Импортиране на модела User и Task
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inclusivehub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "your_secret_key_here"  # Смени го с безопасна стойност

# Инициализация на db с приложението
db.init_app(app)

# Рутове
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    message = request.form["message"]
    return "Thank you, {}. Your message has been received.".format(name)

# Рут за регистрация
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Проверка за съществуващ потребител
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken.")
            return redirect(url_for("register"))

        # Създаване на нов потребител
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")
 # Рут на вход
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print("Attempting login with Username: {} and Password: {}".format(username, password))  # Дебъг информация

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            flash("Login successful!")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password.")
            return redirect(url_for("login"))

    return render_template("login.html")



# Рут за изход
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully.")
    return redirect(url_for("home"))

# Рут за преглед на всички задачи
@app.route("/tasks")
def tasks():
    if "user_id" not in session:
        flash("Please log in to view your tasks.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    user = User.query.get(user_id)
    return render_template("tasks.html", tasks=user.tasks)

# Рут за създаване на нова задача
@app.route("/tasks/new", methods=["GET", "POST"])
def new_task():
    if "user_id" not in session:
        flash("Please log in to create a task.")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        due_date = request.form["due_date"]
        user_id = session["user_id"]

        new_task = Task(
            title=title,
            description=description,
            due_date=datetime.strptime(due_date, "%Y-%m-%d") if due_date else None,
            user_id=user_id
        )
        db.session.add(new_task)
        db.session.commit()
        flash("Task created successfully!")
        return redirect(url_for("tasks"))

    return render_template("new_task.html")

# Рут за редактиране на задача
@app.route("/tasks/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != session.get("user_id"):
        flash("You are not authorized to edit this task.")
        return redirect(url_for("tasks"))

    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form["description"]
        task.due_date = datetime.strptime(request.form["due_date"], "%Y-%m-%d") if request.form["due_date"] else None
        db.session.commit()
        flash("Task updated successfully!")
        return redirect(url_for("tasks"))

    return render_template("edit_task.html", task=task)

# Рут за изтриване на задача
@app.route("/tasks/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != session.get("user_id"):
        flash("You are not authorized to delete this task.")
        return redirect(url_for("tasks"))

    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!")
    return redirect(url_for("tasks"))

# Рут за профила
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_id" not in session:
        flash("Please log in to view your profile.")
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]

        # Добави функционалност за смяна на паролата
        if request.form["password"]:
            user.set_password(request.form["password"])

        db.session.commit()
        flash("Profile updated successfully!")
        return redirect(url_for("profile"))

    return render_template("profile.html", user=user)


# Създаване на таблиците в базата данни
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
with app.app_context():
    db.create_all()
