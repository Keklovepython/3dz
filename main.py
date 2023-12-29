from flask import Flask,render_template,request
import sqlite3

app = Flask('Project123', template_folder="templates", static_folder="static")


def create_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            city TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()


@app.route('/')
def index():
    return render_template("reg.html")

@app.route('/inf')
def info():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    return render_template('inf.html', users=users)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, city) VALUES (?, ?)', (name, city))
        conn.commit()
        conn.close()

        return 'Data has been submitted successfully!'
    return 'Error submitting data.'


if __name__ == "__main__":
    app.run(debug=True)

