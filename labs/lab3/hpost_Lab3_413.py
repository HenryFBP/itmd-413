import time

__info__ = \
    f"""
    Henry Post,
    Lab 03: Bank Account Activty,

    ITMD413,
    IIT Spring 2018,
    Ran on {time.strftime("%c")}
    """

__cont = 'y'


def calculate_interest(b: float, ir: float, p: float = 12) -> float:
    return b + ((b) * (ir / p))


def prompt_password(tries=5) -> bool:

    password = input("Please enter new password:\n > ")
    correct = False

    for i in range(tries, 0, -1):
        if not correct:
            attempt = input("Enter password:\n > ")

            if attempt == password:
                correct = True
            elif tries > 0:
                print(f"Nope. {i - 1} tries left.")
            else:
                print("Too many failed attempts.")
        else:
            break

    if correct:
        print("Correct!")

    return correct


def prompt_balance() -> float:
    return float(input("Input balance in dollars:\n > $"))


def prompt_interest() -> float:
    return (1.0 / 100.0) * float(input("Input interest rate in percent:\n > %"))


def prompt_months() -> int:
    return int(input("Input months to run for:\n > "))


def prompt() -> {}:
    while True:
        try:
            i = prompt_interest()
        except:
            print("Please enter a valid interest value.")
        else:
            break

    while True:
        try:
            b = prompt_balance()
        except:
            print("Please enter a valid dollar value.")
        else:
            break

    while True:
        try:
            m = prompt_months()
        except:
            print("Please enter a valid number of months.")
        else:
            break

    return {"months": m, "interest": i, "balance": b}


inp = "y"

print("Hello!")

prompt_password()

print(f"Enter anything other than {__cont} to quit.")

while len(inp) > 0 and inp[0].upper() == __cont.upper():
    answers = prompt()  # get interest, current balance, and number of months

    interest = answers["interest"]
    months = answers["months"]
    balance = answers["balance"]
    newbal = balance

    for i in range(0, months):
        oldbal = newbal  # to calc difference

        newbal = calculate_interest(newbal, interest)

        print("| Month {m:3d} | ${b:<10.2f} | + ${d:<10.2f}".format(
            m=i + 1, b=newbal, d=(abs(oldbal - newbal))))

        pass

    print(f"Continue? ({__cont}/n)")
    inp = input("> ")

print("Bye!")

print(__info__)
