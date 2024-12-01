import unittest
from app import multiply

class TestApp(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

if __name__ == '__main__':
    unittest.main()