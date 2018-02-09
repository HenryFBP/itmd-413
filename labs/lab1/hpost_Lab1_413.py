import time

__info__ = \
    f"""
    Henry Post,
    1/15/2018,
    Lab 01: Appliance Cost Calculator,
    
    ITMD413,
    IIT Spring 2018,
    Ran on {time.strftime("%x")}
    
    """


def ensure(v, f, e):
    if (f(v)):
        return v
    else:
        raise e


def ensurePositive(v):
    return ensure(v, lambda x: (True if x >= 0 else False), ValueError)


class Appliance:
    name: str = "generic fridge appliance"
    costkWh: float = 0.15
    annualUsage: float = 200.0
    meta: object = None

    def __init__(self, n: str=name, c: float=costkWh, au: float=annualUsage, m: object=None) -> None:
        self.name = n
        self.costkWh = float(c)
        self.annualUsage = float(au)
        self.meta = m

    def totalCost(self) -> float:
        return self.costkWh * self.annualUsage

    def prompt(self) -> None:
        n = input("Name:     > ")

        while True:
            try:
                c = ensurePositive(float(input("$/kWh:    > $")))
            except ValueError:
                print("Please input a valid, non-negative number for $/kWh.")
                continue
            else:
                break

        while True:
            try:
                au = ensurePositive(float(input("kWh/year: > ")))
            except ValueError:
                print("Please input a valid, non-negative number for kWh/year.")
                continue
            else:
                break

        self.__init__(n, c, au)

    def __str__(self) -> str:
        return '"[{:<15}]" ' \
               'uses [{:<7.2f}]kWh/year ' \
               'at [{:<7.2f}]¢/KW, ' \
               'for a total of $[{:<7.2f}]/year.'.format(self.name, self.annualUsage, self.costkWh, self.totalCost())

    def __repr__(self) -> str:
        return str(self)


class Appliances:
    list = []

    def __init__(self, lst=list) -> None:
        self.list = lst

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self) -> int:
        return len(self.list)

    def __iter__(self):
        return self.list.__iter__()

    def peek(self) -> Appliance:
        return self[-1]

    def append(self, a) -> None:
        self.list.append(a)

    def prompt(self) -> None:
        a = Appliance()
        a.prompt()

        self.append(a)

    def costkWhs(self) -> float:
        totCost = 0.0

        for appliance in self.list:
            totCost += appliance.costkWh

        return totCost

    def annualUsages(self) -> float:
        totAU = 0.0

        for appliance in self.list:
            totAU += appliance.annualUsage  # TODO use reduce + lambda to turn these 3 into one-liners

        return totAU

    def totalCosts(self) -> float:
        totCost = 0.0

        for appliance in self.list:
            totCost += appliance.totalCost()

        return totCost

    def __str__(self):
        ret = ""
        ret += f"{len(self)} appliances.\n\n"
        ret += "{:.2f} total cost/kWh annually.\n".format(self.costkWhs())
        ret += "{:.2f} total kWh annually.\n".format(self.annualUsages())
        ret += "${:.2f} total cost annually.\n\n".format(self.totalCosts())

        ret += "Appliance List:\n"

        appliance: Appliance
        for appliance in self.list:
            ret += str(appliance) + "\n"

        return ret


inp = "y"

print("Hello!")

aps = Appliances()

while (len(inp) > 0 and inp[0].upper() == 'Y'):
    print(f"{len(aps)} appliances so far.")

    aps.prompt()
    print("That \"{}\" costs ${:.2f} annually.".format(aps.peek().name, aps.peek().totalCost()))

    print("Enter anything other than 'y' to quit and display statistics.")
    print("Continue? (y/n)")
    inp = input("> ")

print("Summary: \n")
print(aps)

print("Bye!")

print(__info__)
