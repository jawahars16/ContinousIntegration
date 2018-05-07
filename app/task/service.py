import os
import logging
from pkgutil import iter_modules


class TaskService:

    def __init__(self, taskloader):
        self.taskloader = taskloader

    def get_all_tasks(self, category):
        tasks = self.taskloader.load_tasks(category)
        return tasks

    def get_inputs(self, task_id, step_id=None):
        plugin, module_name = task_id.split('@', 1)
        task = self.taskloader.load_task(module_name, plugin)
        return task.get_inputs(task)
