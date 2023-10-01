import unittest
from main import get_question, greetings
import io
import sys
from contextlib import redirect_stdout


class MainTest(unittest.TestCase):
    def test_questions(self):
        question = get_question()
        self.assertEqual(True, isinstance(question, tuple) and len(question) == 2)

    def test_greetings(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            greetings("test", "****")
            output = buf.getvalue()
            self.assertEqual('Вопрос: test\n* * * *\n', output)


if __name__ == '__main__':
    unittest.main()
