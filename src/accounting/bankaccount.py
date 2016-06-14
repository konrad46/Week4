class BankAccount:
    def __init__(self, bank, routing, account):
        self.__bank_name = bank
        self.__routing_number = routing
        self.__account_id = account

    def deposit(self, bank, amt, account, routing):
        print("Depositing "
              "$" + amt + " in " + bank + " Account Number: " + account + " using Routing Number: " + routing)