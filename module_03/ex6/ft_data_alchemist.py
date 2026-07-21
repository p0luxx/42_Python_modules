#!/usr/bin/python3
import random


if __name__ == "__main__":
    players_list = [
            "Alice", "bob", "Charlie", "dylan", "Emma",
            "Gregory", "john", "kevin", "Liam"
            ]
    capitalized_players = [
            name for name in players_list if name == name.capitalize()
            ]
    all_players = [name.capitalize() for name in players_list]
    dictionary = {player: random.randint(1, 666) for player in all_players}
    scores = [dictionary[valor] for valor in dictionary]
    average = sum(scores) / len(players_list)
    high_scores = {
            score: dictionary[score] for score in dictionary
            if dictionary[score] > average
            }
    print(f"Initial list of players: {players_list}")
    print(f"New list with all names capitalized: {all_players}")
    print(f"New list of capitalized names only: {capitalized_players}")
    print(f"Score dict: {dictionary}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")
