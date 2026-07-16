from database import get_connection


class PostgresRepository:
    def get_items(self):
        conn = get_connection()

        cur = conn.cursor()

        cur.execute("SELECT id, name, created_at FROM items ORDER BY id")

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return rows

    def add_item(self, name):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("INSERT INTO items (name) VALUES (%s)", (name,))

        conn.commit()

        cur.close()
        conn.close()
