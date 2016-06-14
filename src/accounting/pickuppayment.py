from src.accounting.paymentmethod import PaymentMethod


class PickUpPayment(PaymentMethod):
    def __init__(self, pay):
        self.__pay = pay

    def pay(self):
        output = "A check for $", str(format(self.__pay, ',.2f')), " is waiting for Adrian Tillman at the PostMaster."
        return output