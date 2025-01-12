"""
.
"""
from random import randrange

class DiceCount():
    """
    Count Dice
    """

    def __init__(self) -> None:
        self.dice_combo: dict[int,int] = {
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0
        }

    def add_number(self, num: int) -> None:
        """
        Add dice
        """
        self.dice_combo[num] += 1

    def get_dict(self) -> dict[int,int]:
        return self.dice_combo

    def percentage(self) -> dict[int, str]:
        """
        Returns percentage. Probability that the dice will land
        """

        total_dict = sum(self.dice_combo.values())

        percentage: dict[int, str] = {key: f"{(self.dice_combo[key] / total_dict) * 100:.2f}%" for key in self.dice_combo}
        return percentage

catan_game = DiceCount()
for i in range(0,64):
    num = randrange(2,13)
    catan_game.add_number(num)


