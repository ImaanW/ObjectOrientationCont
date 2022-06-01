from account import Account,InsufficientFunds
# check balance
try:
    jade_account = Account(250)
    jade_balance = jade_account.check_balance()
    print(jade_balance)


    peter_account = Account(550)
    peter_balance = peter_account.check_balance()
    print(peter_balance)

    # Withdraw balance
    peter_account.withdraw(1000)
    print(peter_account.check_balance()) # 500
except InsufficientFunds as ex:
    print('You have gone overdrawn')
    print(ex)


