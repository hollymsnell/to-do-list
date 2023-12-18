import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS todos;
        """
    )
    conn.execute(
        """
        CREATE TABLE todos (
          id INTEGER PRIMARY KEY NOT NULL,
          task TEXT,
          due_date DATETIME,
          priority TEXT,
          status BOOLEAN
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    todos_seed_data = [
        ("feed pets", "2023-12-18", "high", False),
        ("exercise", "2023-12-18", "medium", False),
        ("organize closet", "2023-12-18", "low", False),
    ]
    conn.executemany(
        """
        INSERT INTO todos (task, due_date, priority, status)
        VALUES (?,?,?,?)
        """,
        todos_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()