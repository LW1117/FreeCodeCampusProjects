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
        if self.balance < amount:
            return False
        self.balance += -amount
        self.ledger.append({"amount": amount, "description": description})
        return True
    
    def get_balance(self):
        return self.balance

    

food = Category("food")
food.deposit(2000, 'hello')
food.withdraw(2000, 'hello')
food.deposit(2000, 'hello')
# food.withdraw(2000, 'hello')
print(food.balance)
 
# def create_spend_chart(categories):
#     pass