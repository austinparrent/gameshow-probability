import random

def probability_test(num_of_tests):
    # determines probability of winning when you change your number choice
    winning_numbers = []
    contestant_decisions = []
    swapped_decisions = []

    # fill in lists with numbers
    for x in range(num_of_tests):
        winning_number = random.randint(1, 3)
        contestant_decision = random.randint(1, 3)
        
        winning_numbers.append(winning_number)
        contestant_decisions.append(contestant_decision)
        
        # represent a swapped decision after game show host reveals a wrong number
        
