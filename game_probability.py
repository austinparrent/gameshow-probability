import random
    
def probability_test(num_of_tests):
    # determines probability of winning when you change your number choice
    winning_numbers = []
    contestant_decisions = []
    swapped_decisions = []
    
    wins = 0
    losses = 0

    # fill in lists with numbers
    for x in range(num_of_tests):
        winning_number = random.randint(1, 3)
        contestant_decision = random.randint(1, 3)
        
        winning_numbers.append(winning_number)
        contestant_decisions.append(contestant_decision)
        
        # represent a swapped decision after game show host reveals a wrong number
        if(contestant_decision == 1):
            if(winning_number == 2):
                swapped_decision = 2
            elif(winning_number == 3):
                swapped_decision = 3
            else:
                swapped_decision = random.randint(2, 3)
        elif(contestant_decision == 2):
            if(winning_number == 1):
                swapped_decision = 1
            elif(winning_number == 3):
                swapped_decision = 3
            else:
                swapped_decision = random.randrange(1, 5, 2)
        elif(contestant_decision ==3):
            if(winning_number == 1):
                swapped_decision = 1
            elif(winning_number == 2):
                swapped_decision = 2
            else:
                swapped_decision = random.randint(1, 2)
            
        swapped_decisions.append(swapped_decision)

    # determine how many times you would have won or lost in a given sample of games
    for x in range(num_of_tests):
        if(winning_numbers[x] == swapped_decisions[x]):
            wins += 1
        else:
            losses += 1
    print("Wins: ", wins, "\nLosses: ", losses, "\n")
    
    # do a simple check to make sure the wins and losses are adding to the total number of tests
    game_check = ((wins+losses) == num_of_tests)
    print("Wins/Losses Check: ", game_check)
