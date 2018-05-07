import logging
import os
from unittest import TestCase
from app.config import Config
from app._common.task_loader import TaskLoader
from app.task.service import TaskService

logging.getLogger().setLevel(logging.DEBUG)

class TestTask(TestCase):

    def setUp(self):
        logging.getLogger().setLevel(logging.DEBUG)
        self.taskloader = TaskLoader(os.path.join(os.path.dirname(__file__).replace('test',''), Config.TASK_DIR))

    def test_load_tasks(self):
        service = TaskService(self.taskloader)
        tasks = service.get_all_tasks('test')
        self.assertEqual(1, len(tasks))
        self.assertEqual(tasks[0].title, 'Test Task')
        self.assertEqual(tasks[0].description, 'This is a test task')

    def test_get_input(self):
        service = TaskService(self.taskloader)
        tasks = service.get_all_tasks('test')
        inputs = service.get_inputs(tasks[0].id)
        self.assertEqual(2, len(inputs))
        self.assertEqual('test1', inputs[0].key)
        self.assertEqual(False, inputs[1].required)
