from src.accounting.employee import Employee
from src.accounting.address import Address
from src.accounting.hourlyemployee import HourlyEmployee
from src.accounting.salariedemployee import SalariedEmployee


class PaymentMethod(Employee, Address, HourlyEmployee, SalariedEmployee):

    def __init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission):
        Employee.__init__(first_name, last_name)
        Address.__init__(street_address, city, state, zip_code)
        HourlyEmployee.__init__(total_pay)
        SalariedEmployee.__init__(commission)

    def pay(self, person):
        person.pay(person)