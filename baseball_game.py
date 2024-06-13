from baseball_game_result import BaseballGameResult


class BaseballGame:
    def __init__(self) -> None:
        super().__init__()
        self.question = ""

    def guess(self, guessNumber) -> BaseballGameResult:
        self.assert_illegal_value(guessNumber)
        return BaseballGameResult(True, 3, 0)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord("0") <= ord(number) <= ord("9"):
                raise TypeError()
        if self.ifDuplicatedNumber(guessNumber):
            raise TypeError()

    def ifDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]
