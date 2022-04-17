# A game based on the American TV show: Let's Make a Deal.

from game_engine import *
from random import randint
from datetime import date, datetime
"""
Procedure:
    1) Game starts
    2) Player picks the case
    3) Host reveals another case, asks player if the player would like to
    switch the case
    4) Player switches or stays
    5) Repeat 2-4 for other players - if any
    5) Open cases for each player. Declare the winner.

Few Notes:
    - Each player has one turn. This can be changed by updating the while loop.
    - Default game has one player and 3 briefcases.
    - Interactive mode is for command-line play, if it is false program will
    randomly choose the inputs.
    - The case host reveals will always be the case with no price, this can be
    changed by removing the if-else check in get_random_case method of the
    GameEngine class.
    - game_data, the dict to return containing game information, is customized
    for default game settings (one player with 3 briefcases).
"""

def play(num_players: int, num_cases: int, interactive: bool) -> None:
    # Introduction
    if interactive:
        print("Welcome to the Game Show!")

    # Initialize
    game = GameEngine(num_players, num_cases)
    host = Host(game)
    players = [Player(game, i+1) for i in range(num_players)]
    player_number = 0
    game_data = {
        "initial_briefcase": -1,
        "revealed_briefcase": -1,
        "switched": False,
        "new_briefcase": -1,
        "wins": False,
        "winning_briefcase": game.get_winning_case_number(),
        "date": date.today().isoformat(),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    # Start
    while player_number < num_players:
        if interactive:
            game.print_cases()

        # Player picks a case
        current_player = players[player_number]
        if interactive:
            case_number = int(input(f"Player {current_player.get_number()}, pick a briefcase: "))
            # Check for case_number validity
            if case_number < 1 or case_number > num_cases:
                raise Exception("Invalid case number")
        else:
            case_number = randint(1, num_cases)

        current_player.pick_case(case_number)
        # update game_data
        game_data["initial_briefcase"] = case_number

        if interactive:
            print(f"Player {current_player.get_number()} picked briefcase {case_number}!")

        # Host reveals a case
        case_to_reveal = host.reveal_case()
        if interactive:
            print(f"Host reveals briefcase {case_to_reveal.get_number()}!")
            if case_to_reveal.get_wins():
                print("The briefcase has the price!")
            else:
                print("The briefcase does not contain the price.")

        # update game_data
        game_data["revealed_briefcase"] = case_to_reveal.get_number()

        # Player decides whether to switch briefcases or not
        if interactive:
            print(f"Player {current_player.get_number()},")
            switch = input(f"Would you like to switch your briefcase? [yes/no] ")
            if switch == "yes":
                new_case_number = int(input("Which briefcase would you like?: "))
                current_player.switch_case(new_case_number)
                print(f"Player {current_player.get_number()} switched to briefcase {new_case_number}!")

                # update game_data
                game_data["switched"] = True
                game_data["new_briefcase"] = new_case_number

            elif switch == "no":
                print(f"Player {current_player.get_number()} decided to not switch the briefcase!")

            else:
                raise Exception("Invalid answer")

        else:
            # Randomly decide if switch briefcase or not
            if randint(0,1) == 1: # switch
                # Randomly pick one of the available cases
                available_cases = game.get_available_case_numbers()
                index = randint(0, len(available_cases) - 1)
                current_player.switch_case(available_cases[index])

                # update game_data
                game_data["switched"] = True
                game_data["new_briefcase"] = available_cases[index]

        player_number += 1

    # Open chosen briefcase(s)
    for current_player in players:
        current_case_number = current_player.get_case_number()
        current_case_status = game.get_case_status(current_case_number, available = False)

        if interactive:
            print(f"Player {current_player.get_number()},")
            print(f"You have briefcase {current_case_number}.")

            # Check player's briefcase
            if current_case_status:
                print(f"Briefcase {current_case_number} contains the price!")
                print(f"Player {current_player.get_number()} wins.")
            else:
                print(f"Briefcase {current_case_number} does not contain the price.")
                print(f"Player {current_player.get_number()} loses.")

        # update game_data
        game_data["wins"] = True if current_case_status else False

    # End
    if interactive:
        print(f"The winning briefcase was {game.get_winning_case_number()}!")
        print("Thank you for playing!")

    return game_data

if __name__ == "__main__":
    game_data = play(1, 3, interactive=True)
    print(game_data)
