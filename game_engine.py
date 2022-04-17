# Game Engine - Organizer + necessary objects
from random import randint
from typing import List

class Briefcase:
    def __init__(self, number: int, wins: bool) -> None:
        self.wins = wins
        self.number = number

    def set_wins(self, wins: bool) -> None:
        self.wins = wins

    def get_wins(self) -> bool:
        return self.wins

    def get_number(self) -> int:
        return self.number


class GameEngine:
    def __init__(self, num_players = 1, num_cases = 3) -> None:
        self.num_players = num_players

        self.picked_cases = {}
        self.available_cases = {}

        for i in range(1, num_cases + 1):
            self.available_cases[i] = Briefcase(i, False)

        # Randomly choose the winnning case
        self.winning_case_number = randint(1, num_cases)
        self.available_cases[self.winning_case_number].set_wins(True)

    def print_cases(self) -> None:
        s = "Available cases: "
        i = 0
        for case_number in self.available_cases:
            s += str(self.available_cases[case_number].get_number()) + " "
            i += 1
        print(s)

    def find_case(self, number: int, available: bool) -> Briefcase:
        if available:
            for case in self.available_cases:
                if self.available_cases[case].get_number() == number:
                    return self.available_cases[case]

            # Look for an exception in picked_cases
            for case in self.picked_cases:
                if self.picked_cases[case].get_number() == number:
                    raise Exception("Case already picked")

        else:
            for case in self.picked_cases:
                if self.picked_cases[case].get_number() == number:
                    return self.picked_cases[case]

            # Look for an exception in picked_cases
            for case in self.available_cases:
                if self.available_cases[case].get_number() == number:
                    raise Exception("Case has not been picked")

        raise Exception("Case not found")

    def get_case_status(self, number: int, available: bool) -> bool:
        return self.find_case(number, available).get_wins()

    def get_winning_case_number(self) -> int:
        return self.winning_case_number

    def update_case(self, number: int, available: bool) -> None:
        # Check if case exists and in the right place
        chosen_case = self.find_case(number, available)
    
        if available:
            self.available_cases.pop(number)
            self.picked_cases[number] = chosen_case
        else:
            self.picked_cases.pop(number)
            self.available_cases[number] = chosen_case

    def get_random_case(self) -> Briefcase:
        available_numbers = list(self.available_cases)
        index = randint(0, len(available_numbers) - 1)

        if available_numbers[index] == self.winning_case_number:
            index += 1
            index %= len(available_numbers)

        # Transfer from available_cases to picked_cases
        chosen_case = self.available_cases.pop(available_numbers[index])
        self.picked_cases[available_numbers[index]] = chosen_case
        return chosen_case

    def get_available_case_numbers(self) -> List[int]:
        return list(self.available_cases)


class Host:
    def __init__(self, game: GameEngine) -> None:
        self.game = game

    def reveal_case(self) -> Briefcase:
        return self.game.get_random_case()


class Player:
    def __init__(self, game: GameEngine, number: int) -> None:
        self.number = number
        self.game = game
        self.case_number = -1

    def get_number(self) -> int:
        return self.number

    def get_case_number(self) -> int:
        return self.case_number

    def pick_case(self, number: int) -> None:
        self.game.update_case(number, available = True)
        self.case_number = number

    def drop_case(self) -> None:
        self.game.update_case(self.case_number, available = False)

    def switch_case(self, number: int) -> None:
        self.drop_case()
        self.pick_case(number)
