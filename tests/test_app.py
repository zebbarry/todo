import pytest
from todo.api import get_tasks, create_task, delete_task, finish_task, undo_task


def test_list_tasks(test_app):
    # Make sure no tasks exist
    assert get_tasks() == []
    # Create some tasks
    create_task("buy milk")
    create_task("buy cookies")
    # Make sure we have 2 tasks now
    assert len(get_tasks()) == 2


def test_unique_task_ids(test_app):
    # Make sure no tasks exist
    assert len(get_tasks()) == 0
    # Create some tasks
    create_task("buy milk")
    create_task("buy cookies")
    # Make sure we have 2 tasks with different ids now
    tasks = get_tasks()
    assert len(set(task.id for task in get_tasks())) == 2


def test_delete_task(test_app):
    # Create a task
    create_task("buy milk")
    [task] = get_tasks()
    delete_task(task.id)
    assert len(get_tasks()) == 0


def test_finish_task(test_app):
    # Create a task
    create_task("buy milk")
    [task] = get_tasks()
    assert not task.done
    finish_task(task.id)
    [task] = get_tasks()
    assert task.done


def test_undo_task(test_app):
    # Create a task
    create_task("buy milk")
    [task] = get_tasks()
    finish_task(task.id)
    [task] = get_tasks()
    assert task.done
    undo_task(task.id)
    [task] = get_tasks()
    assert not task.done
