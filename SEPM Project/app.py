from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            reorder_level INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home page - view all items
@app.route('/')
def index():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Add new item
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        reorder_level = request.form['reorder_level']
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventory (name, quantity, reorder_level) VALUES (?, ?, ?)",
                       (name, quantity, reorder_level))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_item.html')

# Update an item
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        reorder_level = request.form['reorder_level']
        cursor.execute("UPDATE inventory SET name = ?, quantity = ?, reorder_level = ? WHERE id = ?",
                       (name, quantity, reorder_level, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM inventory WHERE id = ?", (id,))
        item = cursor.fetchone()
        conn.close()
        return render_template('update_item.html', item=item)

# Delete an item
@app.route('/delete/<int:id>')
def delete_item(id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
