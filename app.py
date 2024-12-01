import sqlite3
import os
from flask import Flask

app = Flask(__name__)

# Path to the SQLite database
DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'your_database_name.db')

def init_db():
    """Create the database and tables if they do not exist."""
    if not os.path.exists(DATABASE):
        # Connect to the SQLite database (it will create the file if it doesn't exist)
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/')
def index():
    # Initialize the database
    init_db()

    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Get all items from the inventory
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()

    conn.close()

    return f"Inventory: {items}"

if __name__ == '__main__':
    app.run(debug=True)
