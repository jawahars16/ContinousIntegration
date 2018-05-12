import unittest
import os
from unittest import TestCase
from app._common.util import Storage

class TestStorage(TestCase):

    def setUp(self):
        self.storage = Storage(os.path.join(os.path.dirname(__file__), 'work'))

    def test_create_directory(self):
        test_directory = self.storage.create_directory('test_directory')
        self.assertTrue(os.path.exists(test_directory))
