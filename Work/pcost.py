# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        header = f.readline().split(',')
        row = 0
        for line in f:
            row += 1
            data = line.split(',')
            try:
                total_cost += int(data[1]) * float(data[2])
            except ValueError as e:
                print(f'Row {row}: {e}')
                continue
    return total_cost

def portfolio_cost_csv(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rownum, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError as e:
                print(f"Row {rownum}: Couldn't convert: {row}")
                continue
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    #filename = './Work/Data/portfolio.csv'
    #filename = './Work/Data/missing.csv'
    filename = './Work/Data/portfoliodate.csv'

cost = portfolio_cost_csv(filename)
print(f'Total cost {cost}')