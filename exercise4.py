from sys import exit
from pprint import pprint


class Employee(object):


    def enter_data(self):
        self.name = input("Name of employee: ")
        self.hours = input("Hours per week: ")
        self.rate = input("Rate of pay per hour: ")
        var = self.convert()
        return var

    def convert(self):

        try:
            self.hours = float(self.hours)
            self.rate = float(self.rate)

        except:
            print("Error, you must input numbers for the hours and rate.")
            return 'entry_fail'

        else:
            var2 = self.calculations()
            return var2

    def calculations(self):


        if self.hours <= 40:
            self.wage = self.rate * self.hours

            return self

        elif self.hours > 40:
            bonus = (self.hours - 40) * (self.rate * 1.5)
            normal_rate = 40 * self.rate
            self.wage = normal_rate + bonus

            return self
        else:
            raise Exception("Error in Calculations")



class Database(object):


    employee_database = {}

    def view_data(self):


        print("Here is the database:")
        pprint(Database.employee_database)

        answer = input("Please input a name to view their details: ")

        employee_obj = Database.employee_database.get(answer)


        if employee_obj == None:
            print("Please enter a name correctly")
            return self.view_data()

        else:
            print(f"Employee's name {employee_obj.name}")
            print(f"Employee's hours per week: {employee_obj.hours}")
            print(f"Employee's rate of pay per hour: £{employee_obj.rate}")
            print(f"Employee's weekly wage (inc. bonus if applic.): £{round(employee_obj.wage, 2)}")


class Engine(object):

    def __init__(self):
        self.data_base = Database()

    def run_engine(self):

        while True:
            answer = input("Add an employee? (y/n) ")

            if answer == 'y':
                emp = Employee()
                emp = emp.enter_data()

                if emp == 'entry_fail':
                    print("Please try again")

                else:
                    self.data_base.employee_database[emp.name] = emp

            elif answer == 'n':
                answer2 = input("Would you like to view the information entered? (y/n) ")

                if answer2 == 'y':
                    self.data_base.view_data()

                else:
                    exit(0)

            else:
                pass


engine_obj = Engine()
engine_obj.run_engine()
