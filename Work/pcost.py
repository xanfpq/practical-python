# pcost.py
#
# Exercise 1.27
from report import read_portfolio
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in portfolio])

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_file')
    print(f'Total cost {portfolio_cost(argv[1])}')

if __name__ == '__main__':
    main(sys.argv)