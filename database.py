import sqlite3

def create_connection():
    connection = sqlite3.connect("task_manager.db")
    return connection

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task_name TEXT
            )
        """)
        connection.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print("Error:", e)
        connection.rollback()

def insert_data(connection):
    try:
        cursor = connection.cursor()
        tasks = [("1", "Task 1"), ("2", "Task 2"), ("3", "Task 3")]
        cursor.executemany("INSERT INTO tasks (id, task_name) VALUES (?, ?)", tasks)
        connection.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error:", e)
        connection.rollback()

def select_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("Error:", e)
        return []
    

def update_task(connection, task_id, new_task_name):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE tasks SET task_name = ? WHERE id = ?", (new_task_name, task_id))
        connection.commit()
        print("Task updated successfully.")
    except sqlite3.Error as e:
        print("Error:", e)
        connection.rollback()
        connection = sqlite3.connect("task_manager.db")
        update_task(connection, 1, "New Task Name")
        connection.close()

def delete_task(connection, task_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        connection.commit()
        print("Task deleted successfully.")
    except sqlite3.Error as e:
        print("Error:", e)
        connection.rollback()
        



if __name__ == "__main__":
    try:
        connection = sqlite3.connect("task_manager.db")
        create_table(connection)

        # Check if data already exists before inserting
        rows = select_data(connection)
        if not rows:
            insert_data(connection)

        rows = select_data(connection)
        for row in rows:
            print("Task ID:", row[0], ", Task Name:", row[1])

        connection.close()
        print("Connection closed.")

    except sqlite3.Error as e:
        print("Error:", e)

    
