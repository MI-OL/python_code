from io import SEEK_CUR
from random import choice, randrange

def set_simulation():# collects input for number of games to simulate and decision to switch
    while True: # keeps looping until condition breaks loop, i.e. correct input
        try:
            global nb_of_games 
            nb_of_games = int(input('How many games should I simulate? '))
            if nb_of_games <= 0: # check input is a positive integer
                raise ValueError
            break
        except ValueError:
            print('Your input is incorrect, try again. ')
    # input switch or not
    while True:
        global contestant_switches
        contestant_switches = input('Should the contestant switch? ')
        if contestant_switches.istitle():
            contestant_switches = contestant_switches.lower()
        if contestant_switches.lower() in {'yes', 'y'}:
            contestant_switches = True
            print('I keep in mind you want to switch.')
            break
        if contestant_switches.lower() in {'no', 'n'}:
            contestant_switches = False
            print('I keep in mind you don\'t want to switch')
            break
        print('Your input is incorrect, try again. ')
    return nb_of_games, contestant_switches


def simulate(nb_of_games_to_display = 6):# method to run simulation
    nb_of_wins = 0 # set var to count wins for output of simulation
    nb_of_games, contestant_switches = set_simulation() # set vars by calling method
    print('Starting simulation with the contestant', end = ' ')
    if not contestant_switches:# if checks a boolean for True. Not inverts the if statement to check for boolean False. Hence in this instance the if statement checks to see if the boolean variable contestant_switches evaluates to False. If it does than the rest of the function will be executed, i.e. the print statement executes
        print('not', end= '')
    print('switching doors. \n') # output showing if contestant decision to switch
    for i in range(nb_of_games): # for loop to run simulation chosen number of times
        doors = ['A','B','C'] # list of doors
        winning_door = choice(doors) # randomly selects winning door
        first_chosen_door = doors.pop(randrange(3)) # removes contestants first chosen door from list of doors
        if i < nb_of_games_to_display:# has not come to end of loop
            print('\tContestant does not know it, but car 'f'happens to be behind door {winning_door}.')
            print(f'\tContestant chooses door {first_chosen_door}.')
        if not contestant_switches: 
            second_chosen_door = first_chosen_door
        if first_chosen_door == winning_door: # already removed from list of doors.
            opened_door = doors.pop(randrange(2)) # opened door can be random from remaining doors in list as they are both not the winning door, and the winning door has already been removed as the first_chosen_door variable.
            if contestant_switches: # second door is the changed to last remaining door
                second_chosen_door = doors[0]
            else:
                nb_of_wins += 1
        else: # contestant doesn't switch and first chosen door is not the winning door
            doors.remove(winning_door) # winning door removed as host won't open it.
            opened_door = doors[0] # only door remaining as other two have been removed
            if contestant_switches:
                second_chosen_door = winning_door
                nb_of_wins += 1
        if i < nb_of_games_to_display:
            print(f'\tGame host opens door {opened_door}.')
            print(f'\tContestant chooses door {second_chosen_door}', end = ' ')
            if second_chosen_door == winning_door:
                print('and wins.\n')
            else: 
                print('and looses.\n')
        elif i == nb_of_games_to_display:
            print('...')
    print('Contestant has won '
          f'{nb_of_wins / nb_of_games * 100:.2f}% of games.'
         )

simulate()
