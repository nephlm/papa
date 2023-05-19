# May import users


class Accounts:
    """
    cash is positive (usually) for a checking and investment account
    cach is negative (usually) for a credit card

    """

    user_id = int
    institution_id = int
    cash = float


class Institutions:
    name = str
    credentials = str
    plaid_id = str


# plaid user/item key needs to link institution her and user_id, which is
# in Account
# This relationsship needs to be considered.
