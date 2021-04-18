class Budget:
    def __init__(self, **categories):
        self.categories = categories
        
# creating the class methods
    def deposit(self, category, amount):
        self.categories[category] += amount
        print(f"You've deposited {amount} into the {category} category. Current Balance: {self.categories[category]}")

    def withdraw(self, category, amount):
        balance = self.categories[category] - amount
        if(self.categories[category] < amount):
            print(f"Sorry, you have insufficient funds in your account. Currennt balance: {self.categories[category]}")
        else:
            print(f"You've withdrawn {amount} from the {category} category. Current Balance: {balance}")

    def check_balance(self, category):
        print(f"You're current balance for the {category} category is: {self.categories[category]}")

    def transfer(self, amount, transfer_category, receiver_category):
        if(self.categories[transfer_category] < amount):
            print(f'Sorry, you have insufficient funds in your account to make the transfer. kindly top-up. Currennt balance: {self.categories[transfer_category]}')
        else:
            self.categories[transfer_category] -= amount
            self.categories[receiver_category] += amount

            print(f"You've successfully transfered {amount} from the {transfer_category} category into your {receiver_category} category. \n Curent balance: {transfer_category} : {self.categories[transfer_category]}, {receiver_category} : {self.categories[receiver_category]}")
              
# Instantiating my object
expenses = Budget(food=10000, clothing = 5000, entertainment = 2000)

# deposit functionality
expenses.deposit('food', 2000)

# withdrawal functionality
expenses.withdraw('clothing', 2000)

# Withdraw amount that exceeds the balance
expenses.withdraw('entertainment', 3000)

# check balance functionality
expenses.check_balance('entertainment')

# transfer functionality
expenses.transfer(3000, 'clothing', 'entertainment')

# transfer an amount that exceeds the current balance
expenses.transfer(8000, 'entertainment', 'food')

