import logging
import os
from unittest import TestCase
from app.config import Config
from app._common.util import TaskLoader
from app.main import Application


class TestTaskLoader(TestCase):

    def setUp(self):
        self.app = Application()
        
    def tearDown(self):
        self.app.reset()

    def test_resolve_category(self):
        category = self.app.taskloader.__resolve_category__('test', '/')
        self.assertEqual('/test', category)

    def test_resolve_category_without_delimiter(self):
        category = self.app.taskloader.__resolve_category__('test', '')
        self.assertEqual('test', category)

    def test_resolve_classname(self):
        classname = self.app.taskloader.__resolve_classname__('TestClass')
        self.assertEqual('Test Class', classname)

    def test_resolve_classname_camelcase(self):
        classname = self.app.taskloader.__resolve_classname__('testClass')
        self.assertEqual('Test Class', classname)

    def test_resolve_classname_lowercase(self):
        classname = self.app.taskloader.__resolve_classname__('testclass')
        self.assertEqual('Testclass', classname)

    def test_load_tasks(self):
        tasks = self.app.taskloader.load_tasks('test')
        self.assertEqual(1, len(tasks))
        self.assertEqual(tasks[0].title, 'Test Task')
        self.assertEqual(tasks[0].description, 'This is a test task')
