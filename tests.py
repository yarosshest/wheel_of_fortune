import unittest
from game import Game
import io
import sys
from contextlib import redirect_stdout


class MainTest(unittest.TestCase):

    def test_questions(self):
        game = Game()
        game.get_question()
        self.assertEqual(True, game.question != '' and game.answer != '')

    def test_greetings(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.star_answer = ["*", "*", "*", "*"]
            game.greetings()
            output = buf.getvalue()
            self.assertEqual('Вопрос: test\n* * * *\n', output)


if __name__ == '__main__':
    unittest.main()
