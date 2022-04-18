# pcost.py

import sys
from .report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_file')
    print(f'Total cost {portfolio_cost(argv[1])}')

if __name__ == '__main__':
    main(sys.argv)