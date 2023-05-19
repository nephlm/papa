import datetime

# May import accounts


class Stock:
    symbol = str
    price = float
    last_update = datetime.datetime


class Position:
    stock_id = int
    account_id = int
    number = float
    original_cost = float
