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

    @unittest.mock.patch('game.random.choice')
    def test_roll_bankrupt(self, mock_random):
        mock_random.return_value = "Б"
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            with io.StringIO() as buf, redirect_stdout(buf):
                game.roll(1)
                output = buf.getvalue()
            self.assertEqual('Вращайте барабан\nУ вас банкрот. Очки сгорают, а ход переходит к другому игроку\n',
                             output)

    @unittest.mock.patch('game.random.choice')
    def test_roll_next(self, mock_random):
        mock_random.return_value = "next"
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            with io.StringIO() as buf, redirect_stdout(buf):
                game.roll(1)
                output = buf.getvalue()
            self.assertEqual('Вращайте барабан\nХод переходит к другому игроку\n',
                             output)

    @patch('builtins.input', return_value="t")
    @unittest.mock.patch('game.random.choice')
    def test_roll_score_true(self, mock_random, mock_input):
        mock_random.return_value = 500
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            with io.StringIO() as buf, redirect_stdout(buf):
                game.roll(1)
                output = buf.getvalue()
            self.assertEqual('Вращайте барабан\n'
                             'Вы заработали 500 очков\n'
                             'Назовите букву\n'
                             'Вы отгадали. Откройте пожалуйста такие буквы в слове\n'
                             't * * t\n', output)

    @patch('builtins.input', return_value="k")
    @unittest.mock.patch('game.random.choice')
    def test_roll_score_false(self, mock_random, mock_input):
        mock_random.return_value = 500
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            with io.StringIO() as buf, redirect_stdout(buf):
                game.roll(1)
                output = buf.getvalue()
            self.assertEqual('Вращайте барабан\n'
                             'Вы заработали 500 очков\n'
                             'Назовите букву\n'
                             '* * * *\n', output)

    def test_result(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            game = Game()
            game.question = "test"
            game.answer = "test"
            game.star_answer = ["*", "*", "*", "*"]
            game.break_main = 1
            game.scores[1] = 500
            with io.StringIO() as buf, redirect_stdout(buf):
                game.result()
                output = buf.getvalue()
            self.assertEqual('Победил Игрок-1\n'
                             'Набранное количество очков 500\n', output)


if __name__ == '__main__':
    unittest.main()
