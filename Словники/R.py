class Bank:
    def __init__(self):
        self.accounts = {}

    def deposit(self, name, amount):
        if name not in self.accounts:
            self.accounts[name] = 0
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name not in self.accounts:
            self.accounts[name] = 0
        if self.accounts[name] >= amount:
            self.accounts[name] -= amount
            return True
        else:
            return False

    def balance(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            return "ERROR"

    def transfer(self, from_name, to_name, amount):
        if from_name not in self.accounts:
            self.accounts[from_name] = 0
        if to_name not in self.accounts:
            self.accounts[to_name] = 0
        if self.accounts[from_name] >= amount:
            self.accounts[from_name] -= amount
            self.accounts[to_name] += amount
            return True
        else:
            return False

    def income(self, percent):
        for name in self.accounts:
            if self.accounts[name] > 0:
                self.accounts[name] += int(self.accounts[name] * percent / 100)


def process_operations(operations):
    bank = Bank()
    result = []

    for operation in operations:
        if operation[0] == "DEPOSIT":
            bank.deposit(operation[1], int(operation[2]))
        elif operation[0] == "BALANCE":
            result.append(bank.balance(operation[1]))
        elif operation[0] == "TRANSFER":
            if not bank.transfer(operation[1], operation[2], int(operation[3])):
                result.append("ERROR")
        elif operation[0] == "INCOME":
            bank.income(int(operation[1]))
        elif operation[0] == "Exit":
            break

    return result


operations = [
    ["DEPOSIT", "Ivanenko", "100"],
    ["INCOME", "5"],
    ["BALANCE", "Ivanenko"],
    ["TRANSFER", "Ivanenko", "Petrenko", "-50"],
    ["WITHDRAW", "Petrenko", "100"],
    ["BALANCE", "Petrenko"],
    ["BALANCE", "Sydorenko"],
    ["Exit"]
]

results = process_operations(operations)
for res in results:
    print(res)
