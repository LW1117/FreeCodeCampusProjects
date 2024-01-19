class Category:
    balance = 0

    def __str__(self):
        no_of_stars = int((30 - len(self.category_name)) / 2)
        title_line = f'*{"*" * no_of_stars }{self.category_name}{"*" * no_of_stars }'
        content = ''
        space = 0
        for x in self.ledger:
            space = 30 - len(x["description"][:23]) - len(str(x["amount"])[:7])
            content += (f'{x["description"][:23]}{space * " "}{str(x["amount"])[:7]}\n')

        output = f'{title_line}\n{content}Total:{self.balance:.2f}'
        return output

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.amount = amount
        self.balance += amount
        self.description = description
        self.ledger.append({"amount": float("{:.2f}".format(amount)), "description": description})
    
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

def create_spend_chart(category_list):
    bargraph = 'Percentage spent by category\n'
    graph = {
        100:['100|'],
        90:[' 90|'],
        80:[' 80|'],
        70:[' 70|'],
        60:[' 60|'],
        50:[' 50|'],
        40:[' 40|'],
        30:[' 30|'],
        20:[' 20|'],
        10:[' 10|'],
        0:['  0|'],
    }
    Percentages = []
    category_names = [x.category_name for x in category_list]
    temp = 0
    spend_sum = 0
    for category in category_list:
        for item in category.ledger:
            if str(item['amount'])[0] == '-':
                spend_sum += item['amount']
        Percentages.append(spend_sum)
        spend_sum = 0
    total_spend = sum(Percentages)
    # print(total_spend)
    for item in range(len(Percentages)):
        Percentages[item] = round(round(Percentages[item] * 100 / total_spend) /10 ) * 10
    # print(Percentages)

    for item in range(0,110,10):
        # print(item)
        for percentage_no in range(len(Percentages)):
            if Percentages[percentage_no] >= 0:
                graph[item].append('o ')
            Percentages[percentage_no] -= 10
    
    



    for x in graph:
        for y in graph[x]:
            bargraph += f'{y} '
        bargraph += '\n'
    bargraph += '    -'
    for percentage_no in Percentages:
        bargraph += '---'
    bargraph += '\n'

    max_length = max(len(name) for name in category_names)
    for i in range(max_length):
        bargraph += '     '
        for name in category_names:
            if i < len(name):
                bargraph += f'{name[i]}  '
            else:
                bargraph += '   '  # Padding for shorter names
        bargraph += '\n'
    return bargraph

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
print(actual)
print(entertainment)

# print(create_spend_chart([food, clothing, auto]))
 
# def create_spend_chart(categories):
#     pass