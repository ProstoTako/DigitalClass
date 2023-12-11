def get_balance(name: str, transactions: list):
    balance = 0
    for transact in transactions:
        if transact['name'] == name:
            balance += transact['amount']
    return balance


def count_debts(names: list, amount: int, transactions: list):
    dict_homies = dict()
    for name in names:
        debt = get_balance(name, transactions) - amount
        if debt >= 0:
            debt = 0
        else:
            debt = abs(debt)
        dict_homies[name] = debt
    return dict_homies
