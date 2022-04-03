# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))

def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for r in portfolio:
        report.append((r['name'], r['shares'], prices[r['name']], prices[r['name']] - r['price']))
    return report

def print_report(report):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    report = [headers, ('-' * 10,) * len(headers)] + report
    for line, row in enumerate(report):
        name, shares, price, change = row
        if line < 2:
            print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
        else:
            print(f'{name:>10s} {shares:>10d} ${price:>9.2f} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} portfolio_file prices_file')
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)