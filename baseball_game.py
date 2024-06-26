from baseball_game_result import BaseballGameResult


class BaseballGame:
    def __init__(self) -> None:
        super().__init__()
        self.question = ""

    def guess(self, guessNumber) -> BaseballGameResult:
        self.assert_illegal_value(guessNumber)
        if self.is_solved(guessNumber):
            return self.get_sucess_game_result()
        else:
            return self.get_unsolved_game_result(guessNumber)

    def is_solved(self, guessNumber):
        return guessNumber == self.question

    def get_sucess_game_result(self):
        return BaseballGameResult(True, 3, 0)

    def get_unsolved_game_result(self, guessNumber):
        strikes = 0
        balls = 0
        for i in range(len(self.question)):
            if self.question.find(guessNumber[i]) == i:
                strikes += 1
            elif self.question.find(guessNumber[i]) > -1:
                balls += 1
        return BaseballGameResult(False, strikes, balls)

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
