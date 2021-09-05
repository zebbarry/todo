"""API functions to interact with Todo tasks."""

from todo.models import Task, db


def get_tasks() -> list:
    return Task.query.all()


def create_task(body: str) -> None:
    """
    Add task to the database

    :param body: Name of task
    :return: None
    """
    new_task = Task(body=body)

    db.session.add(new_task)
    db.session.commit()


def delete_task(task_id: int) -> None:
    """
    Delete a task from the database

    :param task_id: Id of the task to delete
    :return: None
    """
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()


def finish_task(task_id: int) -> None:
    """
    Mark a task as done

    :param task_id: Id of the task to mark as done
    :return: None
    """
    task_to_finish = Task.query.get_or_404(task_id)
    task_to_finish.done = True
    db.session.commit()


def undo_task(task_id: int) -> None:
    """
    Mark a task as not done

    :param task_id: Id of the task to mark as not done
    :return: None
    """
    task_to_finish = Task.query.get_or_404(task_id)
    task_to_finish.done = False
    db.session.commit()
