from flask import Flask, render_template,request,redirect,session
import sqlite3

app = Flask(__name__)
app.secret_key = "devhubsecret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database/db.sqlite3")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username,password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid login"

    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        import sqlite3
        conn = sqlite3.connect("database/db.sqlite3")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username,password) VALUES (?,?)",
            (username,password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect("/login")

@app.route("/create", methods=["GET","POST"])
def create_snippet():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        title = request.form["title"]
        code = request.form["code"]
        author = session["user"]

        conn = sqlite3.connect("database/db.sqlite3")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO snippets (title,code,author) VALUES (?,?,?)",
            (title,code,author)
        )

        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("create_snippet.html")

@app.route("/snippets")
def view_snippets():

    conn = sqlite3.connect("database/db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM snippets")
    snippets = cursor.fetchall()

    conn.close()

    return render_template("view_snippet.html", snippets=snippets)

@app.route("/delete/<int:id>")
def delete_snippet(id):

    conn = sqlite3.connect("database/db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM snippets WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/snippets")

if __name__ == "__main__":
    app.run(debug=True)