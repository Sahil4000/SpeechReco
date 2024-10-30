from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

# Database initialization
def init_db():
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        account_number TEXT,
        phone_number TEXT,
        address TEXT,
        aadhaar_card TEXT,
        withdraw_amount REAL
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json
    full_name = data.get("full_name")
    account_number = data.get("account_number")
    phone_number = data.get("phone_number")
    address = data.get("address")
    aadhaar_card = data.get("aadhaar_card")
    withdraw_amount = data.get("withdraw_amount")

    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO submissions (full_name, account_number, phone_number, address, aadhaar_card, withdraw_amount) VALUES (?, ?, ?, ?, ?, ?)",
        (full_name, account_number, phone_number, address, aadhaar_card, withdraw_amount)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Form data saved successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
