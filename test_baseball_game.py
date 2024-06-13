from unittest import TestCase
from baseball_game import BaseballGame
from baseball_game_result import BaseballGameResult


class TestBaseballGame(TestCase):
    def setUp(self):
        self.game = BaseballGame()
        super().setUp()

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def test_return_solve_result_if_matched_number(self):
        self.game.question = "123"
        result: BaseballGameResult = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.solved)
        self.assertEqual(3, result.strikes)
        self.assertEqual(0, result.balls)
