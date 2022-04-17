# Let's Make a Deal - Monty Hall Problem

## Introduction
A game engine, organizer and simulator based on the American TV show: Let's Make a Deal. The simulator collects data from each game instance and writes them into a .csv file.

## Description
The game has a host, a contestant and three briefcases. One of the briefcases contains the prize and as the contestant, the aim is to find the winning briefcase. The procedure is as follows:
* Game starts - "Welcome to the Game Show!"
* Host asks contestant to pick a briefcase
* Contestant picks a briefcase
* Host reveals another briefcase that does not have the prize
* Contestant either stays with the initial briefcase or switches to the third one
* Host reveals contestant's final briefcase
* Contestant wins/loses depending on whether the final briefcase has the prize or not

To run the game interactively, default settings are one contestant with 3 briefcases, but this can easily be changed by updating the play() call under the if __name__ == "__main__" condition of game_show. Setting the "interactive" parameter to False will let the computer automatically run a game process and return its data.

Running the game_simulator will run the game in automatic mode for 2000 times, and save the data to a .csv file. The number of running the game can be changed by simply updating the simulate() function under the if __name__ == "__main__" condition in game_simulator.

The game is written in Python - and therefore to run the game on your local environment you have to have a Python interpreter installed. Additionally, to simulate the game and collect data, the data analysis tool Pandas has been used, so that has to be installed as well.

## Disclaimer
Note that there may still be bugs, as this is almost a prototype version and is aimed for training/demonstrating basic coding ability. Please do not hesitate to reach out if any bug/error has been encountered. I am still working on this project and I would be happy to hear any feedback.
