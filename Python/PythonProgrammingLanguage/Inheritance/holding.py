# holding.py

import csv


class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    with open(filename, "r") as f:
        rows = csv.reader(f)
        header = next(rows)  # skip the header
        portfolio = []
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
            portfolio.append(h)

    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
