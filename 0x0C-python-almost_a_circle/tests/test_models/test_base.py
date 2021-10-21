from models.base import Base
import unittest

class Test_base(unittest.TestCase):

    def test_base(self, id=10):
        if id is None:
            self.assertIsNone(id)
        else:
            self.assertTrue(id)
