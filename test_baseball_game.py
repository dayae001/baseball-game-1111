from unittest import TestCase

from baseball_game import BaseballGame


class TestBaseballGame(TestCase):
    def test_exception_when_input_is_none(self):
        self.game = BaseballGame()
        with self.assertRaises(TypeError):
            self.game.guess(None)
