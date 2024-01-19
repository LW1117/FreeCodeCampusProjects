class Category:
    balance = 0
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.amount = amount
        self.balance += amount
        self.description = description
        self.ledger.append({"amount": -amount, "description": description})
    
    def withdraw(self, amount, description = ''):
        self.amount = amount
        self.description = description
        if not self.check_funds(amount):
            return False
        self.balance += -amount
        self.ledger.append({"amount": amount, "description": description})
        return True
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {other_category.category_name}')
        other_category.deposit(amount, f'Transfer from {self.category_name}')
        return True
    
    def check_funds(self,amount):
        if self.balance < amount:
            return False
        return True

food = Category("food")
travel = Category("travel")
food.deposit(2000, 'hello')
food.withdraw(2000, 'hello')
food.deposit(2000, 'hello')
food.transfer(1000,travel)
# food.withdraw(2000, 'hello')
print(food.ledger)
print(travel.balance)
print(travel.check_funds(1000))
 
# def create_spend_chart(categories):
#     pass