class Category:
    balance = 0

    def __str__(self):
        no_of_stars = int((30 - len(self.category_name)) / 2)
        title_line = f'{"*" * no_of_stars }{self.category_name}{"*" * no_of_stars }'
        content = ''
        space = 0
        for x in self.ledger:
            space = 30 - len(x["description"][:23]) - len(str(x["amount"])[:7])
            content += (f'{x["description"][:23]}{space * " "}{str(x["amount"])[:7]}\n')

        output = f'{title_line}\n{content}Total:{self.balance}'
        return output

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.amount = amount
        self.balance += amount
        self.description = description
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ''):
        self.amount = amount
        self.description = description
        if not self.check_funds(amount):
            return False
        self.balance -= amount
        self.ledger.append({"amount": -amount, "description": description})
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

# food = Category("food")
# travel = Category("travel")
# food.deposit(2000, 'hello')
# food.withdraw(2000, 'hello')
# food.deposit(2000, 'hello')
# food.transfer(1000,travel)
# # food.withdraw(2000, 'hello')
# print(food.ledger)
# print(travel.balance)
# print(travel)

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

# print(create_spend_chart([food, clothing, auto]))
 
# def create_spend_chart(categories):
#     pass