"""URLs for our application."""

from flask import redirect, render_template, request, Response
from todo import app

from todo.api import get_tasks, create_task, delete_task, finish_task, undo_task


@app.route("/")
def tasks_list():
    """
    Get a list of all tasks in the database at '/'

    :return: Rendered HTML page
    """
    tasks = get_tasks()
    # Render the HTML page located in "templates/application.html"
    # Passing tasks as a variable, so it can be used in the template
    return render_template("application.html", tasks=tasks)


@app.route("/task", methods=["POST"])
def task_create() -> Response:
    """
    Create a task in the database at '/task' with a POST request

    :return: Rendered HTML page
    """
    body = request.form["body"]

    create_task(body)

    # Redirect user to the main page, so the new task will be displayed
    return redirect("/")


@app.route("/delete/<int:task_id>")
def task_delete(task_id: int) -> Response:
    """
    Delete a task in the database at '/delete/<int:task_id>' with a GET request

    :return: Rendered HTML page
    """
    delete_task(task_id)

    # Redirect user back to the main page, so the list of tasks will be updated
    return redirect("/")


@app.route("/done/<int:task_id>")
def task_done(task_id: int) -> Response:
    """
    Complete a task in the database at '/done/<int:task_id>' with a GET request

    :return: Rendered HTML page
    """
    finish_task(task_id)

    return redirect("/")


@app.route("/undo/<int:task_id>")
def task_undo(task_id: int) -> Response:
    """
    Undo a task in the database at '/undo/<int:task_id>' with a GET request

    :return: Rendered HTML page
    """
    undo_task(task_id)

    return redirect("/")
