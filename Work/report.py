# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    '''Ŕead data of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for line, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                portfolio.append(record)
            except ValueError as e:
                print(f'Line {line} ({row})with errors: {e}')
                continue
    return portfolio

def read_prices(filename):
    '''Read data of a price file'''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        line = 0
        for row in rows:
            line += 1
            try:
                prices[row[0]] = float(row[1])
            except ValueError as e:
                print(f'Line {line} ({row})with errors: {e}')
                continue
            except IndexError as e:
                print(f'Line {line} ({row})with errors: {e}')
                continue
    return prices

def make_report(portfolio, prices):
    '''Make report with stock and prices'''
    report = []
    for r in portfolio:
        report.append((r['name'], r['shares'], prices[r['name']], prices[r['name']] - r['price']))
    return report

#portfolio = read_portfolio('./Work/Data/portfolio.csv')
portfolio = read_portfolio('./Data/portfoliodate.csv')
prices = read_prices('./Data/prices.csv')
report = make_report(portfolio, prices)

header = [('Name', 'Shares', 'Price', 'Change'), ('-'*10,)*4]
report = header + report
line = 0
for name, shares, price, change in report:
    line += 1
    if line <= 2:
        print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
    else:
        print(f'{name:>10s} {shares:>10d} ${price:>9.2f} {change:>10.2f}')

#pprint(portfolio)
#pprint(prices)
#pprint(report)

'''
total = 0
for data in portfolio:
    total += data['shares'] * data['price']
print(f'Total {total:0.2f}')
'''