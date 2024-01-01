def get_balance(name: str, transactions: list) -> int:
    balance = 0
    for transact in transactions:
        if transact['name'] == name:
            balance += transact['amount']
    return balance


def count_debts(names: list, amount: int, transactions: list) -> dict:
    debt_homies = {name: amount - get_balance(name, transactions) for name in names}
    debt_homies = {name: 0 if debt < 0 else debt for name, debt in debt_homies.items()}
    return debt_homies