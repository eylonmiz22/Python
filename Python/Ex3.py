from functools import reduce
import datetime
from types import FunctionType
import re


print("Made by\nDaniel:  316421262"
      "\nEylon:   206125411")
print("---------------------------------------------- Question 1 ----------------------------------------------")


def sum_list_functional(lst):
    return reduce(lambda x, y: x+y, lst)


def sum_lst_imperative(lst):
    total = 0
    for k in lst:
        total += k
    return total


my_list = [1, 2, 3, 4, 5]
print(my_list)
print("Imperative sum: " + str(sum_lst_imperative(my_list)))
print("Functional sum: " + str(sum_list_functional(my_list)))
print("---------------------------------------------- Question 2a ----------------------------------------------")


def question2():
    number = 0
    while number >= 0:
        number = int(input("Enter a Number: "))
        if number % 2 == 0:
            print("Even")
        elif number > 0:
            print("Odd")
    print("All Done!")


question2()
print("---------------------------------------------- Question 2b ----------------------------------------------")
print("Answer: Define a Dictionary from each label to a specific function serving as a Label Content")


def func1():
    print("label 1 content")


def func2():
    print("label 2 content")


labelDictionary = {1: func1, 2: func2}


def goto_example(label):
    while label not in labelDictionary:
        label = int(input("Enter a Label between 1-2 for the Example: "))

    labelDictionary[label]()


def question2b():
    number = int(input("Enter a Label Number: "))
    goto_example(number)


question2b()

print("---------------------------------------------- Question 3a ----------------------------------------------")


class Account:

    def __init__(self, name, bank_number, balance, credit_frame=1500):
        self.Name = str(name)
        self.BankNumber = str(bank_number)
        self.Balance = float(balance)
        self.CreditMax = int(credit_frame)

    def deposit(self, money):
        self.Balance += int(money)
        print("Deposit Successful!"
              "\t" + str(money) + " Shekels have been deposited into " + str(self.Name) + "'s Account.")

    def withdraw(self, money):
        if self.Balance >= money:
            self.Balance -= int(money)
            print("Withdrawal Successful!"
                  "\t" + str(money) + " Shekels have been withdrawn from " + str(self.Name) + "'s Account.")
            return money

    def check_balance(self):
        print("Balance for " + str(self.Name) + "'s Account: " + str(self.Balance))

    class _Decorators(object):
        @classmethod
        def transfer_decorator(cls, func):
            def inner(*args, **kwargs):
                func(*args, **kwargs)
                now = datetime.datetime.now()
                print('Money Transfer Date and Time: ' + now.strftime("%Y-%m-%d %H:%M:%S"))

            return inner

    @_Decorators.transfer_decorator
    def transfer(self, other, amount):
        if self.Balance >= amount:
            other.deposit(self.withdraw(amount))
            print("<\n" + str(amount) + " Shekels Have Been transferred to " + str(other.Name) +
                  " Successfully! \n>")

        else:
            print("Amount to transfer exceeds account Balance!")

    def print_account(self):
        print("\nAccount Details:\n[Name: " + str(self.Name) + "| Bank Number: " + str(self.BankNumber) + "| Balance: "
              +
              str(self.Balance) + "| Max Credit: " + str(self.CreditMax) + "]")


acc1 = Account("itamar", 111, 1500, 2300)
acc2 = Account("eylon", 222, 2000)
acc3 = Account("danil", 333, 2500)

acc1.print_account()
acc2.print_account()
print("---------------------------------------------- Question 3b ----------------------------------------------")
acc1.transfer(acc2, 1500)
acc1.print_account()
acc2.print_account()
print("---------------------------------------------- Question 3c ----------------------------------------------")
bank = [acc1, acc2, acc3]
generator_expression = (acc.Balance for acc in bank)


def balance_generator(lst):
    n = 0
    while n < len(lst):
        yield lst[n]
        n += 1


for acc in balance_generator(bank):
    acc.check_balance()
print("---------------------------------------------- Question 4 ----------------------------------------------")
method_list = [x for x, y in Account.__dict__.items() if type(y) == FunctionType]
deposit_Account = getattr(Account, str(method_list[1]))
withdraw_Account = getattr(Account, method_list[2])
balance_Account = getattr(Account, method_list[3])
transfer_Account = getattr(Account, method_list[4])

acc4 = Account("Ariel", 111, 1500, 2300)
acc5 = Account("Daniel", 222, 5000)

balance_Account(acc4)
balance_Account(acc5)

deposit_Account(acc4, 450)
withdraw_Account(acc5, 2000)
transfer_Account(acc4, acc5, 950)  # transfer will trigger withdrawal print because withdraw is used inside.

balance_Account(acc4)
balance_Account(acc5)
print("---------------------------------------------- Question 5 ----------------------------------------------")
f = open("words.txt", "r+")


def read_text_generator(txt):
        for line in txt:
            for word in line.split():
                if not re.search('e', word):
                    yield word


print("All the words in the Text with no letter e in them:")
for i in read_text_generator(f):
    print(i)
f.close()
print("---------------------------------------------- Question 6 ----------------------------------------------")


def f1(x, y=[]):
    y.append(x)
    return sum(y)


def f2(x, y=None):
    if y is None:
        y = []
    y.append(x)
    return sum(y)


print("Using f1: " + str(f1(10)))
print("Using f1: " + str(f1(30)))

print("Using f2: " + str(f2(10)))
print("Using f2: " + str(f2(30)))

print("Answer: as long as you don't put arg2 of the functions then the default values will be "
      "implemented."
      "\nIn f1: if I keep calling the function with one argument it will add x to the default array"
      "\nwith Memory of the last Call and will return the Sum of all x's given in the history of the entire Run."
      "\nin f2: if I keep calling the function with one argument it will check if y is default"
      "\nand if it is it will RESET the Array and always return x as a Sum "
      "\nIf you put a ready array into arg2 the functions are the same.")
