#Task 1
class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expenses = 0

#Task 2 

    def get_name(self):
        return self.__name
    
    def get_budget(self):
        return self.__budget
    
    def get_remaining_budget(self):
        return self.__budget - self.__expenses
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_budget(self, new_budget):
        if new_budget > 0:
            self.__budget = new_budget
        else:
            raise ValueError("Budget must be a positive number")

#Task 3

    def add_expense(self, amount):
        if amount > 0 and amount <= self.get_remaining_budget():
            self.__expenses += amount
        else:
            raise ValueError("The expense must be less than or equal to our current budget")
        
#Task 4

    def display_category_summary(self):
        return f'Category: {self.get_name()}, Approved budget: {self.get_budget()}, Remaining budget: {self.get_remaining_budget()}'

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
print(food_category.display_category_summary())