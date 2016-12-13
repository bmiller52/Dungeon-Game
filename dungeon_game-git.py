import random
import sys
from sys import exit

def start_game():
    player_trail = []

    if_sword = [0]
    help1 = [0]
    help2 = [0]

    cell = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
            (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

    def start_again():
        while True:
            play_again = raw_input('Do you want to play again? y/n ').lower()
            if play_again == 'y':
                start_game()

            if play_again == 'n':
                print(' ')
                print('Ok. Hope you had fun!')
                print(' ')
                sys.exit()

            else:
                print('That\'s not a valid answer!')
                print(' ')
                continue

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
          printed_map.append('O|')

        elif current_room in player_trail:
          printed_map.append('*|')

        else:
            printed_map.append('_|')


        if current_room[1] == 6:
          printed_map.append('\n')
        count += 1

      print(''.join(printed_map))

    player_location, monster_location, monster2_location, sword_location, escape_location = right_location()

    print(' ')
    print('Wlecome to the Dungeon game!')
    print('You are in a 6 by 6 grid. There are 2 monsters, one sword, and one escape.')
    print(' ')
    print("You've been captured by Those Generic Bad Guys. After beating you over the top of the head, ")
    print("they throw you in That Generic Dungeon. Inside, you are allowed to wander throughout each ")
    print("of the rooms, and discover that there are 36 rooms total, all connected in a 6 by 6 grid. ")
    print("Since you are a creative Generic Young Hero, you form a torch by scrounging around on the ")
    print("dirty dungeon floor. However, you aren't quite as skilled as you thought, and your torch ")
    print("is weak. The further you go, the more the torch falls apart. After exploring the dungeon ")
    print("for some time, you realize that there's an exit in one of the rooms, and several Generic ")
    print("Monsters lurking in the dark. Plan your path carefully.")
    print(' ')
    print('Simply type in (W) UP, (D) RIGHT, (S) DOWN, or (A) LEFT. Then press enter')
    print(' ')

    player_trail.append(player_location)

    def show_monster_location():
        print('The First Monsters Location Is {}'.format(monster_location))

    def show_monster_location2():
        print('The Second Monsters Location Is {}'.format(monster2_location))

    print_map()

    while True:

        print('(Q) for quit, (H) for help')
        move = raw_input('Which Way Do You Want To Move? ').upper()

        if move == 'H':
            print(' ')
            print('You Just Revealed One Monster, Type \'MORE H\' To Reveal Another Monster.')
            show_monster_location()
            help1[0] = 1

        if move == 'MORE H':
            print(' ')
            print('Both Monsters Have Been Revealed')
            show_monster_location2()
            help2[0] = 1

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
            print('Great! You Have Found The Sword')
            print('Now If You Run Into A Monster You Can Slay It')
            print(' ')

            if_sword[0] = 1

        if player_location == monster_location or player_location == monster2_location:
            if 0 in if_sword:
                print(' ')
                print('Oh No! The Monster Got You!')
                print(' ')
                start_again()

            if 1 in if_sword:
                print(' ')
                print('Hooray! You Have Just Slayed The Monster!')
                print('But You Lost The Sword')
                print(' ')

                if_sword[0] = 0

        if player_location == escape_location:
            print(' ')
            print('Congratulations! You Escaped The Dungeon!')
            print('The Escape Was {}'.format(escape_location))
            print(' ')
            start_again()

        player_trail.append(player_location)

        monster_status = 'Unknown'
        if 1 in help1:
            monster_status = monster_location

        monster2_status = 'Unknown'
        if 1 in help2:
            monster2_status = monster2_location

        print(' ')
        print('The First Monsters Location: {}'.format(monster_status))
        print('The Seconds Monsters Location: {}'.format(monster2_status))
        print(' ')

        if move == 'Q':
            print(' ')
            print('Thanks for playing!')
            print(' ')
            sys.exit()

        if move == 'D':
            print('You Moved Right!')

        if move == 'A':
            print('You Moved Left!')

        if move == 'S':
            print('You Moved Down!')

        if move == 'W':
            print('You Moved Up!')

        print_map()

start_game()
