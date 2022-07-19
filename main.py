# NOTE THIS NEEDS TO BE RUN IN PYTHON CONSOLE

# Parent CLass : User
# Child Class : Bank
# Stores details about the bank balance
# Stores details about the amounts
# Allows for deposits, withdraw, view_balance

# Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_personal_details(self):
        print("Personal details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)




# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance available : $", self.balance)
        else:
            self.balance -= self.amount
            print("Account balance has been updated : $", self.balance)

    def view_balance(self):
        self.show_personal_details()
        print("Account balance : $", self.balance)


user1 = Bank("Badr", 14, "Male")
