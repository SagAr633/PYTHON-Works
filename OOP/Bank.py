# bank_name - static
# account creation(name,ac_no)
# deposit(amount,balance)
# withdraw(amnt)
class Bank:
    bank_name='HDFC'
    def acnt_creation(self,ac_ho_name,acc_no):
        self.ac_ho_name=ac_ho_name
        self.acc_no=acc_no
        self.minbal=10000
        self.balance=self.minbal
    def deposit(self,amnt):
        self.amnt=amnt
        self.balance=self.balance+self.amnt
        print('Your',Bank.bank_name,'Account has been credited with amount',self.amnt)
        print('Your Current Balance is',self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print('Insufficent Fund')
        else:
            self.balance=self.balance-self.amount
            print('Your',Bank.bank_name,'Account debited by amount',self.amount)
            print('Your Availabe Balance is',self.balance)
a1=Bank()
a1.acnt_creation('Sagar',875653675)
a1.deposit(7000)
a1.withdraw(3000)

