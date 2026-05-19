import mysql.connector

# ---------------- CONNECT ----------------
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bloodglucose_dp",
        port=3306   # or 3307 (match your MySQL)
    )

# ---------------- SAVE DATA ----------------
def save_data(data):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO records (name, age, glucose, bmi, status)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, data)
    conn.commit()

    cursor.close()
    conn.close()

# ---------------- DELETE ----------------
def delete_record(record_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM records WHERE id=%s", (record_id,))
    conn.commit()

    cursor.close()
    conn.close()

# ---------------- FETCH ----------------
def fetch_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data