from _typeshed import Self
from . import Expense

class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if (self.sum_expenses+item < self.budget):
           self.expenses.append(item)
           self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return len(self.expenses) + len(self.overages)

    def __inter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    def __next__(self):
        try:
            return self.iter_e__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()


def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses: ' + str(len(myBudgetList)))

    for entry in myBudgetList:
        print(entry)

if __name__ == "__main__":
    main()



