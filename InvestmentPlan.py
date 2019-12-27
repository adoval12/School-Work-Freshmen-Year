#
#
# InvestmentPlan  
#
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

def avg_price(prices):
    """input a list of prices and the function will return the average
       of the prices
    """
    average = 0
    for i in prices:
        average += (i / len(prices))
    return average

def std_dev(prices):
    standard_deviation = 0
    for i in prices:
        standard_deviation += (((i - avg_price(prices)) ** 2) / len(prices))
    standard_deviation = (standard_deviation ** 0.5)
    return standard_deviation

def max_day(prices):
    max0 = 0
    max_day = 0
    for i in range(len(prices)):
        if max0 > prices[i]:
            max0 = max0
        else:
            max0 = prices[i]
            max_day = i
    return max_day

def any_below(prices, integer_threshold):
    count = 0
    for i in prices:
        if i > integer_threshold:
            count += 1
    if count == len(prices):
        return False
    else:
        return True

def find_plan(prices):
    buyday = 0
    sellday = 0
    difference = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if (prices[j] - prices[i]) > difference:
                buyday = i
                sellday = j
                difference = (prices[j] - prices[i])
            else:
                buyday = buyday
                sellday = sellday
                difference = difference
    return [buyday, sellday, difference]
    
    
    


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            standard_deviation = std_dev(prices)
            print('The standard deviation is', standard_deviation)
        elif choice == 5:
            maxday = max_day(prices)
            print('The max price is', prices[maxday], 'on day', maxday)
        elif choice == 6:
            integer_threshold0 = int(input('Enter the threshold: '))
            if any_below(prices, integer_threshold0) == True:
                print("There is at least one price below", integer_threshold0)
            else:
                print("There are no prices below", integer_threshold0)
        elif choice == 7:
            plan = find_plan(prices)
            print('Buy on', plan[0], 'at price', prices[plan[0]])
            print('sell on', plan[1], 'at price', prices[plan[1]])
            print('Total profit:', plan[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
