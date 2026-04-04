def create_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS canada_computers (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            product_price REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )


def save_price(cursor, name, price):
    cursor.execute(
        "INSERT INTO canada_computers (product_name, product_price) VALUES (?, ?)",
        (name, price),
    )


def get_last_price(cursor, name):
    cursor.execute(
        "SELECT product_price FROM canada_computers WHERE product_name = ? ORDER BY id DESC LIMIT 1",
        (name,),
    )

    result = cursor.fetchone()
    return result[0] if result else None


def get_recent_db_entries(cursor):
    cursor.execute("SELECT * FROM canada_computers ORDER BY id DESC LIMIT 10")
    return cursor.fetchall()
