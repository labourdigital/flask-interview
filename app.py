import sqlite3

from flask import Flask, jsonify, request

from db import setup_db

app = Flask(__name__)

# Initialize the DB
setup_db()


@app.route("/api/user", methods=["GET"])
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return jsonify(
            {"id": user[0], "name": user[1], "email": user[2], "country": user[3]}
        )
    else:
        raise ValueError("User not found")


if __name__ == "__main__":
    app.run(debug=True)
