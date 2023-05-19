import datetime

# May import Account


class Transactions:
    """
    CC charges are transaction that have a negative value
    CC Payments are transaction with positive value
    Direct Deposits are transaction with a positive value
    Outgoing checks have a negative value.
    """

    account_id = int
    execution_date = datetime
    description = str
    amount = float
