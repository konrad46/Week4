from src.accounting.employee import Employee
from src.accounting.timecard import TimeCard

HOURS = 8
OVERTIME = 1.5


class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, rate, weekly_dues):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        self.__rate = rate
        self.__time_card = []

    def get_hourly_rate(self, rate):
        return self.__rate

    def clock_in(self, date, start_time):
        time_start = TimeCard(self, date, start_time)
        self.__time_card.append(time_start)

    def clock_out(self, date, end_time):
        time_end = TimeCard(self, date, end_time)
        self.__time_card.append(time_end)

    def get_pay(self, start_time, end_time, rate):
        total_hours = 0
        for hours in self.__time_card:
            total_hours += hours

        if total_hours <= HOURS:
            total_pay = (HOURS * rate)
        else:
            overtime_pay = ((total_hours - HOURS) * OVERTIME * rate)
            regular_pay = (HOURS * rate)
            total_pay = overtime_pay + regular_pay
        return total_pay