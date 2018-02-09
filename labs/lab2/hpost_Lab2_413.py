import time

__info__ = \
    f"""
    Henry Post,
    1/15/2018,
    Lab 02: BMI Calculator,

    ITMD413,
    IIT Spring 2018,
    Ran on {time.strftime("%c")}

    """


def BMI(weight: float, height: float) -> float:
    return (weight * 703 / (height ** 2))

def BMIRank(bmi: float):
    if(bmi > 25):
       return "overweight"
    elif(bmi > 18.5):
        return "optimal"
    else:
        return "underweight"

def promptWeight() -> float:
    n = float(input("Input weight in pounds:\n > "))
    return n

def promptHeight() -> float:
    s = input("Input height: (eg. 5\"11)\n > ").replace("'",'') # get height in foot+inches w/o single quotes
    sA = s.split("\"") # split by double quote
    inches = (float(sA[0]) * 12) + float(sA[1])
    return inches

def prompt() -> {}:

    while True:
        try:
            w = promptWeight();
        except:
            print("Please enter a valid weight value.")
        else:
            break

    while True:
        try:
            h = promptHeight();
        except:
            print("Please enter a valid height value.")
        else:
            break

    return {"weight":w,"height":h}

inp = "y"

print("Hello!")

while (len(inp) > 0 and inp[0].upper() == 'Y'):
    print("Enter anything other than 'y' to quit.")

    hw = prompt()
    bmi = BMI(hw["weight"], hw["height"])
    print(f"BMI is {bmi:.2f}. You are '{BMIRank(bmi)}' according to the BMI system.")

    print("Continue? (y/n)")
    inp = input("> ")

print("Bye!")

print(__info__)
