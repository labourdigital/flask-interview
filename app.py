import sqlite3

from flask import Flask, jsonify, request

from db import setup_db

app = Flask(__name__)

# Initialize the DB
setup_db()


@app.route("/api/transaction", methods=["GET"])
def get_transaction():
    transaction_id = request.args.get("id")
    conn = sqlite3.connect("transactions.db")

    cursor = conn.cursor()
    query = f"SELECT * FROM transactions WHERE id = {transaction_id}"
    cursor.execute(query)
    transaction = cursor.fetchall()

    if transaction:
        return jsonify(transaction)
    else:
        raise ValueError("Transaction not found")


if __name__ == "__main__":
    app.run(debug=True)
