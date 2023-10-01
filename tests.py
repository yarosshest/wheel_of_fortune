import unittest
from main import get_question


class MainTest(unittest.TestCase):
    def test_questions(self):
        question = get_question()
        self.assertEqual(True, isinstance(question, tuple) and len(question) == 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
