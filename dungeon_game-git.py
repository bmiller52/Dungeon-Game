import random
import sys
from sys import exit

player_trail = []

if_sword = [0]

cell = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
        (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
        (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

def right_location():
    start_location = random.choice(cell)
    monster_location = random.choice(cell)
    monster2_location = random.choice(cell)
    sword_location = random.choice(cell)
    escape_location = random.choice(cell)

    if monster2_location == start_location or escape_location == start_location:
        return right_location()

    if monster_location == monster2_location:
        return right_location()

    if sword_location == start_location or sword_location == monster_location or sword_location == monster2_location or sword_location == escape_location:
        return right_location()

    if monster_location == escape_location or monster_location == start_location or monster2_location == escape_location:
        return right_location()

    return start_location, monster_location, monster2_location, sword_location, escape_location

def print_map():

  count = 0
  printed_map = []

  while count < len(cell):
    current_room = cell[count]

    if current_room == player_location:
		printed_map.append('X|')

    elif current_room in player_trail:
		printed_map.append('.|')

    else:
		printed_map.append(' |')

    if current_room[1] == 6:
		printed_map.append('\n')
    count += 1

  print(''.join(printed_map))

player_location, monster_location, monster2_location, sword_location, escape_location = right_location()

print(' ')
print('Wlecome to the Dungeon game!')
print('You are in a 6 by 6 grid. There are 2 monsters, one sword, and one escape.')
print('Simply type in (W) UP, (D) RIGHT, (S) DOWN, or (A) LEFT. Then press enter')
print(' ')

player_trail.append(player_location)

print_map()

while True:

    move = raw_input('Which way do you want to move? ').upper()

    if move == 'D' and player_location[1] < 6:
        player_location = player_location[0], player_location[1] + 1

    elif move == 'W' and player_location[0] > 1:
        player_location = player_location[0] - 1, player_location[1]

    elif move == 'A' and player_location[1] > 1:
        player_location = player_location[0], player_location[1] - 1

    elif move == 'S' and player_location[0] < 6:
        player_location = player_location[0] + 1, player_location[1]

    if player_location == sword_location:
        print(' ')
        print('Great! You have found the sword')
        print('Now if you run into a monster you can slay it')
        print(' ')

        if_sword[0] = 1

    if player_location == monster_location or player_location == monster2_location:
        if 0 in if_sword:
            print('Oh no! The Monster got you!')
            print(' ')
            break

        if 1 in if_sword:
            print(' ')
            print('Hooray! You have just killed the monster')
            print('But you lost the sword')
            print(' ')

            if_sword[0] = 0

    if player_location == escape_location:
        print('Yay! You escaped!')
        print(' ')
        break

    player_trail.append(player_location)

    print(' ')
    print_map()
