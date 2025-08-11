from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("data/attacks.db")
    c = conn.cursor()
    c.execute("SELECT ip, attack_type, timestamp FROM attacks ORDER BY timestamp DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    attacks = get_data()
    return render_template("index.html", attacks=attacks)

if __name__ == "__main__":
    app.run(debug=True)
