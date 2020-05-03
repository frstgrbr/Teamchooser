#!/bin/python3

# import 'choice' for randomized selection of players
from random import choice

# define an empty variable where players will be populated in
players = []
# access the text file players.txt to add players to the variable 'players'
file = open('players.txt', 'r')
# read player names from the text file and adds them to 'players' separated by line
players = file.read().splitlines()
# print the complete list of players
print(players)

# define an empty variable where team names will be assigned randomly
teamnames = []
# access the text file teams.txt to add players to the variable 'players'
file = open('teams.txt', 'r')
# read team names from the text file and add them to 'teamnames'
teamnames = file.read().splitlines()

# Create three empty teams; teamA, teamB, and teamC
teamA = []
teamB = []
teamC = []

# loops that randomly adds players to one of the three teams
# prints the assignment and players left available to choose from
# players are appended to the associated team and then removed from the master list
# loop breaks if there are less than or equal to 0 players left to assign
while len(players) > 0:
    playerA = choice(players)
    print(playerA)
    teamA.append(playerA)
    players.remove(playerA)
    print('Players left:', players)

# break the loop if there is an odd number of players
    if players == []:
        break

    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print('Players left:', players)

    # break the loop if there is an odd number of players
    if players == []:
        break

    playerC = choice(players)
    print(playerC)
    teamC.append(playerC)
    players.remove(playerC)
    print('Players left:', players)

# chooses a random team name from teams.txt
teamAname = choice(teamnames)
teamBname = choice(teamnames)
teamCname = choice(teamnames)

# prints the resulting randomly assigned team names and players
print(teamAname, teamA)
print(teamBname, teamB)
print(teamCname, teamC)