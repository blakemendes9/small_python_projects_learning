import sys

'''
DEFINING COLLATZ CONJECTURE

The Collatz conjecture is a famous, unproven mathematical problem proposed by Lothar Collatz in 1937.

The Rules:

Take any positive integer (n) and apply these two rules:
1. If (n) is even, divide it by 2 (n / 2).
2. If (n) is odd, multiply it by 3 and add 1 (3n + 1).
Repeat this process with each new result. The conjecture states that every positive integer will 
eventually reach 1, entering the repeating loop of 4 -> 2 -> 1
'''

#This function will conduct the necessary steps
def steps(number):
    if number <= 0:
        raise ValueError
    
    value = number #Sets value to be formulated
    steps_taken = 0 #Given steps taken
    while True:
        if value == 1:
            break
        if value % 2 == 0:
            steps_taken += 1
            value = value / 2
        elif value % 2 != 0:
            steps_taken += 1
            value = (3 * value) + 1
    return steps_taken

def main():
    while True:
        user_number = input('Please enter a number: ')
        try:
            print(f'Steps taken: {steps(int(user_number))}')
            break
        except ValueError:
            print('Please enter a valid number')

main()