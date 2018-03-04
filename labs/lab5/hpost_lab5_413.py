from copy import deepcopy
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

_options[_option_gross_all] = "Gross payroll report for all employees"
_options[_option_gross_one] = "Gross payroll report for one employee"
_options[_option_add] = "Add employee"
_options[_option_delete] = "Delete employee"
_options[_option_modify] = "Modify employee"
_options[_option_quit] = "Quit"


class Employee:
    def __init__(self, fname, lname, rate, hours):
        self.fname = fname
        self.lname = lname
        self.rate = rate
        self.hours = hours

    def __str__(self):
        return f"{self.fname:8s} {self.lname:10s}: ${self.rate:5.02f} at {self.hours:5.02f}h"

    def weeklyRate(self):
        return self.rate * self.hours


def highest_cost(employees):
    """
    Given a list of Employee objects, return the index of the one that costs the most.
    """
    x = 0

    highest_e: Employee = employees[x]

    for i in range(len(employees)):
        if employees[i].weeklyRate() > employees[x].weeklyRate():
            x = i

    return x


def sort_by_highest_cost(employees):
    """
    Given a list of Employee objects, sort them by their costs, high to low.
    """
    sorted = []
    emps = deepcopy(employees)

    while (emps):  # while original list has elements
        x = highest_cost(emps)  # get pos of highest
        e = emps[x]  # record it
        del emps[x]  # delete it
        sorted.append(e)  # append it

    return sorted

def employee_by_name(name, employees):

    try:
        narr = name.split(" ")[0:2]
        fname, lname = narr
    except ValueError as e:
        return None


    for e in employees:
        e: Employee
        if e.fname == fname and e.lname == lname:
            return e


def payroll_report(employees):
    """
    Given a list of Employee objects, print an overview of payroll data.
    """

    employees = sort_by_highest_cost(employees)

    er_strs = {}  # employee report strings
    totalcost = 0.0

    for e in employees:  # get total cost of paying ALL employees
        e: Employee

        totalcost += e.weeklyRate()  # for averages or percents later

    header = ("| {:8} {:9} : {:6} at {:6} | {:7} | {:9} |".format("First", "Last", "Rate", "hr/wk", "perc", "cost/wk"))
    div = ''.join("-" for i in range(len(header)))

    print(sprint_center(div, "[ Gross Payroll Report ]"))
    print(header)
    print(div)

    for e in employees:
        e: Employee

        percentCost = e.weeklyRate() / totalcost  # how much does person X cost out of 100%?

        s = "| "  # a report string unique to that employee

        s += str(e) + " | "  # add the employee's normal data
        s += f"{percentCost*100:6.02f}% | "  # add their percentage cost
        s += f"${e.weeklyRate():<8.02f} | "  # add how much the employee costs per week

        print(s)

    print(div)

    return employees


def parse_employee_line(line):
    """
    Turn a single line of text into an Employee.
    """
    fname, lname, rate, hours = line.split(" ")[0:4]

    return Employee(fname, lname, float(rate), float(hours))


def sprint_center(src, innie):
    """
    Given a src string, put 'innie' in the middle of it.
    Example: sprint_center("+---_---+","hey") -> "+--hey--+"
    """

    # print(f"Wanna put '{innie}' inside of '{src}'")

    src = [char for char in src]
    innie = [char for char in innie]

    mid = len(src) // 2

    in_pos = mid - (len(innie) // 2)

    j = 0
    for i in range(in_pos, in_pos + len(innie)):
        src[i] = innie[j]
        j += 1

    return ''.join(src)


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

def payroll_report_all_employees(employees):
    payroll_report(employees)

def payroll_report_one_employee(employees):
    n = input("Enter employee name:\n > ")

    e = employee_by_name(n, employees)

    if e is not None:
        payroll_report_all_employees([e])
    else:
        print(f"Name '{n}' not found.")

        names = [(e.fname + " " + e.lname) for e in employees]
        names.sort()

        print("Possible names:")

        for name in names:
            print(name)

def add_employee(employees):

    while True:
        try:
            fname = input("Enter first name:\n > ")
            break
        except Exception as e:
            print("Invalid first name.")

    while True:
        try:
            lname = input("Enter last name:\n > ")
            break
        except Exception as e:
            print("Invalid last name.")

    while True:
        try:
            rate = float(input("Enter hourly rate:\n > "))
            break
        except Exception as e:
            print("Invalid hourly rate.")

    while True:
        try:
            hours = float(input("Enter hours per week:\n > "))
            break
        except Exception as e:
            print("Invalid hours per week.")

    employees.append(Employee(fname, lname, rate, hours))


_optionfns = {}

_optionfns[_option_gross_all] = payroll_report_all_employees
_optionfns[_option_gross_one] = payroll_report_one_employee
_optionfns[_option_add] = add_employee
_optionfns[_option_delete] = lambda x: print("Not implemented")
_optionfns[_option_modify] = lambda x: print("Not implemented")
_optionfns[_option_quit] = lambda x: (print(__info__), exit(0))

if __name__ == '__main__':

    print("Hello!")

    employees = parse_employee_txt("./employees.txt")

    for employee in employees:
        print(employee)

    choice = -1

    while True:
        if choice is _option_quit:
            print("Goodbye!")
            break

        for i in _options:  # display the options
            option = _options[i]
            print(f"{i}) {option}")

        choice = int(input(" > "))  # get choice
        if choice in _optionfns:
            _optionfns[choice](employees)  # execute choice
        else:
            print(f"'{choice}' isn't a valid option.")

    print(__info__)
