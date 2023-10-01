import unittest
from game import Game
import io
from contextlib import redirect_stdout
from unittest.mock import patch
from game import random


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

    @patch('builtins.input', return_value="test")
    def test_call_word_true(self, mock_input):
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            with io.StringIO() as buf, redirect_stdout(buf):
                game.call_word(1)
                output = buf.getvalue()
            self.assertEqual('Назовите слово целиком\nПоздравляю, вы ответили правильно!\nОтвет test\n', output)

    @patch('builtins.input', return_value="false")
    def test_call_word_false(self, mock_input):
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            with io.StringIO() as buf, redirect_stdout(buf):
                game.call_word(1)
                output = buf.getvalue()
            self.assertEqual('Назовите слово целиком\nК сожалению, вы ошиблись. Вы проиграли\n', output)


if __name__ == '__main__':
    unittest.main()
