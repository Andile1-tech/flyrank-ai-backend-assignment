from database import get_connection


class SQLiteRepository:
    def __init__(self):
        self.create_table()
        self.seed_tasks()

    def create_table(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done BOOLEAN NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def seed_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM tasks")
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.executemany(
                """
                INSERT INTO tasks (title, done)
                VALUES (?, ?)
                """,
                [
                    ("Learn FastAPI", 0),
                    ("Connect SQLite database", 0),
                    ("Complete FlyRank assignment", 0),
                ],
            )

            conn.commit()

        conn.close()

    def get_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        conn.close()

        return tasks

    def get_task_by_id(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,),
        )

        task = cursor.fetchone()

        conn.close()

        return task

    def add_task(self, title):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO tasks (title, done)
            VALUES (?, ?)
            """,
            (title, 0),
        )

        conn.commit()
        conn.close()

    def update_task(self, task_id, title, done):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET title = ?, done = ?
            WHERE id = ?
            """,
            (title, done, task_id),
        )

        conn.commit()

        updated = cursor.rowcount

        conn.close()

        return updated

    def delete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,),
        )

        conn.commit()

        deleted = cursor.rowcount

        conn.close()

        return deleted
