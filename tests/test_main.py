import unittest

from engine.main import Engine


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()

    def test_hello(self):
        self.assertEqual(self.engine.calculate_total(3), 27)
