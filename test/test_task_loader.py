import logging
import os
from unittest import TestCase
from app.config import Config
from app._common.task_loader import TaskLoader


class TestTaskLoader(TestCase):

    def setUp(self):
        logging.getLogger().setLevel(logging.DEBUG)
        self.taskloader = TaskLoader(os.path.join(
            os.path.dirname(__file__).replace('test', ''), Config.TASK_DIR))

    def test_resolve_category(self):
        category = self.taskloader.__resolve_category__('test', '/')
        self.assertEqual('/test', category)

    def test_resolve_category_without_delimiter(self):
        category = self.taskloader.__resolve_category__('test', '')
        self.assertEqual('test', category)

    def test_resolve_classname(self):
        classname = self.taskloader.__resolve_classname__('TestClass')
        self.assertEqual('Test Class', classname)

    def test_resolve_classname_camelcase(self):
        classname = self.taskloader.__resolve_classname__('testClass')
        self.assertEqual('Test Class', classname)

    def test_resolve_classname_lowercase(self):
        classname = self.taskloader.__resolve_classname__('testclass')
        self.assertEqual('Testclass', classname)

    def test_load_tasks(self):
        tasks = self.taskloader.load_tasks('test')
        self.assertEqual(1, len(tasks))
        self.assertEqual(tasks[0].title, 'Test Task')
        self.assertEqual(tasks[0].description, 'This is a test task')
