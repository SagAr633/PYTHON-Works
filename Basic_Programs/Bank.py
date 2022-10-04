fixed_amount=100000

withdraw=int(input('Enter the Amount you want to withdraw '))

balance=fixed_amount-withdraw

if withdraw>fixed_amount:
    print("Insufficent Balance")
else:
    print('Balance', balance)

