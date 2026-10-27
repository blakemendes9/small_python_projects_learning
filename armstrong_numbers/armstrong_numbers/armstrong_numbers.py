import sys

'''
Determines if number is Armstrong Number:
Example of an Armstrong Number: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
Example of a number != Armstrong Number = 10 != 1^2 + 0^2 = 1
'''

def is_armstrong_number(number):
    #number_string (str): Transforms integer value to string for length
    #digit (int): Gets length of number
    #count (int): Totals the amount of each digit of number to the power of len(number)
    number_string = str(number)
    digit = len(number_string)
    count = 0

    #Calculates each digit
    for char in number_string:
        count += int(char) ** digit

    #Returns True if Armstrong Number
    if number == count:
        return True
    #Returns False if not Armstrong Number
    return False

def main():
    while True:
        user_number = input('Please enter a number: ')
        try:
            check_value = is_armstrong_number(int(user_number))
            if check_value:
                print('Your number is an Armstrong Number')
            else:
                print('Your number is not an Armstrong Number')
            break
        except ValueError:
            print('Please enter a valid number')

main()