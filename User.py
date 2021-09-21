# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


# Create a file with the User class, including the __init__ and make_deposit methods

# Add a make_withdrawal method to the User class

# Add a display_user_balance method to the User class

# Create 3 instances of the User class

# Have the first user make 3 deposits and 1 withdrawal and then display their balance

# Have the second user make 2 deposits and 2 withdrawals and then display their balance

# Have the third user make 1 deposits and 3 withdrawals and then display their balance

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name,"account balance",self.account_balance)
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("Transfering",amount,"from",self.name,"to",other_user.name)

Jay = User("Jay Pritchett","jaypritchett@Pritchettsclosets.com")
Gloria = User("Gloria Pritchett","spicycolumbian@gmail.com")
Claire = User("Claire Dunphy","toomanytequilas@yahoo.com")

Jay.make_deposit(1000)
Jay.make_deposit(1000)
Jay.make_deposit(1000)
Jay.make_withdrawal(330)
Jay.display_user_balance()

Gloria.make_deposit(1000)
Gloria.make_deposit(1000)
Gloria.make_withdrawal(330)
Gloria.make_withdrawal(330)
Gloria.display_user_balance()

Claire.make_deposit(1000)
Claire.make_withdrawal(330)
Claire.make_withdrawal(330)
Claire.make_withdrawal(330)
Claire.display_user_balance()

Jay.transfer_money(Claire,600)
Jay.display_user_balance()
Claire.display_user_balance()
