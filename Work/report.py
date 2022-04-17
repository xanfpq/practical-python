# report.py
#
# Exercise 2.4
import sys
from stock import Stock
from fileparse import parse_csv
import tableformat
from portfolio import Portfolio
import logging
import os

logging.basicConfig(
    filename = 'app.log',      # Name of the log file (omit to use stderr)
    filemode = 'a',            # File mode (use 'a' to append)
    level    = logging.DEBUG,  # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    format   = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portfolio = Portfolio.from_csv(
            lines,
            **opts
        )
        return portfolio

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
        report.append((r.name, r.shares, prices[r.name], prices[r.name] - r.price))
    return report

def print_report(report, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    if isinstance(formatter, tableformat.HTMLTableFormatter): formatter.open() 
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        formatter.row([ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ])
    if isinstance(formatter, tableformat.HTMLTableFormatter): formatter.close()

def portfolio_report(portfolio_filename, prices_filename, format='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(format)
    print_report(report, formatter)

def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    elif len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        raise SystemExit(f'Usage: {argv[0]} portfolio_file prices_file')

if __name__ == '__main__':
    log = logging.getLogger(os.path.basename(__file__))
    log.info('Exetute')
    main(sys.argv)