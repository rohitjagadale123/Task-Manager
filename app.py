from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_name = request.form.get("task-name")
        task_description = request.form.get("task-description")

        try:
            connection = database.create_connection()  # Open a connection
            database.insert_task(connection, task_name, task_description)
            connection.commit()  # Commit changes to the database
            connection.close()   # Close the connection
            return redirect(url_for("index"))
        except Exception as e:
            return "Error: " + str(e)

    else:
        try:
            connection = database.create_connection()  # Open a connection
            rows = database.select_data(connection)
            connection.close()   # Close the connection
            return render_template('index.html', tasks=rows)
        except Exception as e:
            return "Error: " + str(e)
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        new_task_name = request.form.get("new-task-name")
        # Update the task with the new name using your database functions
        return redirect(url_for("index"))

    # Retrieve task data using the task_id and render an edit page

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    try:
        connection = database.create_connection()
        database.delete_task(connection, task_id)
        connection.commit()
        connection.close()
        return redirect(url_for("index"))
    except Exception as e:
        return "Error: " + str(e)


if __name__ == "__main__":
    app.run(debug=True)
