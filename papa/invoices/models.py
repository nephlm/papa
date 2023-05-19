import datetime

# may import transactions


class invoices:
    """
    Implied invoices are invoices based off credit card transaction (or check payments)
    rather than having a proper bill that was received (e.g. Netflix vs Pepco)
    """

    transaction_id = int
    vendor_id = int
    date_due = datetime
    date_issued = datetime
    minimum_amount_due = float
    amount_due = float
    implied = False


class Vendor:
    name = str
    description = str
    regular_billing_cycle = True
    billing_cycle_days = int
    has_implied_invoices = False
