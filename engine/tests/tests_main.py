import unittest

from engine.main import Engine


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()

    def test_hello(self):
        self.assertEqual(self.engine.main(new ), "main.py -h")
