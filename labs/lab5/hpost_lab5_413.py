import time

__info__ = \
    f"""
    Henry Post,
    Lab 05: Payroll Processing

    ITMD413,
    IIT Spring 2018,
    Ran on {time.strftime("%c")}
    """

_option_gross_all = 0
_option_gross_one = 1
_option_add = 2
_option_delete = 3
_option_modify = 4
_option_quit = 5


_options = {}

_options[_option_gross_all] =   "Gross payroll report for all employees"
_options[_option_gross_one] =   "Gross payroll report for one employee"
_options[_option_add] =         "Add employee"
_options[_option_delete] =      "Delete employee"
_options[_option_modify] =      "Modify employee"
_options[_option_quit] =        "Quit"

__cont = 'y'


class Employee:

    def __init__(self, fname, lname, rate, hours):
        self.fname = fname
        self.lname = lname
        self.rate = rate
        self.hours = hours

    def __str__(self):
        return f"{self.fname:8s} {self.lname:10s}: ${self.rate:3.02f} at {self.hours:3.02f}h"


def parse_employee_line(line):
    """
    Turn a single line of text into an Employee.
    """
    fname, lname, rate, hours = line.split(" ")[0:4]

    return Employee(fname, lname, float(rate), float(hours))


def parse_employee_txt(filepath):
    """
    Parse a flat text file representing a list of Employees.
    :param filepath: The location of the file.
    :return: A list of Employees.
    """
    emps = []

    with open(filepath, "r") as file:
        for line in file:
            emps.append(parse_employee_line(line))

    return emps


if __name__ == '__main__':
    employees = parse_employee_txt("./employees.txt")



    for employee in employees:
        print(employee)

    choice = -1

    while True:
        if choice is _option_quit:
            print("Goodbye!")
            break

        for i in _options:
            option = _options[i]
            print(f"{i}) {option}")

        choice = int(input(" > "))