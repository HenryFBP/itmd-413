import time
from random import *

__info__ = \
    f"""
    Henry Post,
    Lab 04: Lotto

    ITMD413,
    IIT Spring 2018,
    Ran on {time.strftime("%c")}
    """

__cont = 'y'
__sd = {True: "√", False: "×"}


def generate_nums(bot: int = 0, top: int = 99, n: int = 3) -> {}:
    """
    Generate an {n}-long list of numbers between {bot} and {top}.
    """
    return [randint(bot, top) for i in range(n)]


def prompt_guesses(bot: int = 0, top: int = 99, n: int = 3) -> {}:
    """
    Generate an {n}-long list of numbers between {bot} and {top} from user input.
    """
    print(f"Enter '{n}' numbers as guesses.\n"
          f"Invalid numbers will be ignored, and I will keep\n"
          f"asking you until I get enough.\n"
          f"Examples: \n"
          f"'1 2 3 [ENTER] 4 5', or \n"
          f"'1 2 3 4 5', or \n"
          f"'1 [ENTER] 2 [ENTER] 3 [ENTER] ...'")

    nums = []
    inp = None

    # keep asking them until list is large enough
    while len(nums) < n:
        inp = input(" > ")
        inp = inp.replace(",", " ").replace(";", " ")  # strip away undesired chars

        # if they enter a list of numbers
        if len(inp.split(" ")) > 1:
            # print(f'Their list: {str(inp.split(" "))}')

            # go through their list
            idx = 0
            for item in inp.split(" "):
                item = item.replace(" ", "")  # strip whitespace

                # print(f"item {idx} is {item}")

                # try to treat it as a number
                try:
                    if int(item) >= bot and int(item) <= top:
                        nums.append(int(item))
                        idx += 1
                    else:
                        print(f"'{inp}' is not between {bot} and {top}")
                except:
                    if len(item) > 0:  # if it isn't an empty string
                        print(f"'{item}' is not a whole number.")

                        if idx > 0:
                            print(f"However, we did get your previous {idx} items and any after it.")
                            idx = 0

        # else, assume they have entered one number.
        else:
            try:
                if int(inp) >= bot and int(inp) <= top:
                    nums.append(int(inp))
                else:
                    print(f"'{inp}' is not between {bot} and {top}")
            except:
                print(f"'{inp}' is not a whole number.")

        # if they're partially done, show them what they got so far.
        if len(nums) < n:
            print(f"Guesses so far: {str(nums[0:n])}")

    return nums[0:n]


def prompt_numbers() -> int:
    """
    Get how many numbers lotto game should have from the user.
    """
    return int(input("How many numbers should this lotto game have?\n > "))


def prompt_bounds() -> (int, int):
    """
    Get the bounds of the lotto numbers.
    """
    print("Enter the lower and upper bounds that this game should have, separated by a space.")

    inp = input().split(" ")
    return (int(inp[0]), int(inp[1]),)


def check_matches(guesses, actual) -> {}:
    """
    Checks a list of guesses against the actual results.
    :param guesses: List of guessed numbers.
    :param actual: List of lotto's result numbers.
    :return: List of True/False that tells you which numbers match.
    """
    return [guesses[i] == actual[i] for i in range(len(guesses))]


def __main__():
    """
    Main function.
    """
    inp = "y"

    print("Hello!")
    n = None

    while True:
        try:
            n = prompt_numbers()
        except:
            print("Input a valid number of lotto balls.")
        else:
            if n <= 0:
                print("Input a positive number of lotto balls.")
            else:
                break

    while True:
        try:
            b = prompt_bounds()
            bot = b[0]
            top = b[1]
        except:
            print("Input valid lotto top & bottom.")
        else:
            if top <= bot:
                print("Top can't be lower than bottom, and vice-versa.")
            else:
                break



    print(f"Enter anything other than {__cont} to quit.")

    while len(inp) > 0 and inp[0].upper() == __cont.upper():
        correct = 0  # assume they are not a winner

        lotto = generate_nums(bot, top, n)  # generate some numbers
        guesses = prompt_guesses(bot, top, n)  # ask them to guess
        matches = check_matches(guesses, lotto)  # generate T/F array

        maxlen = len(str(top))  # to format things
        formats = (" {:^" + str(maxlen) + "} ")  # format specifier for one number.
        # Will make things look like:
        # [  3   2   4   5  ]
        prefs = ("{:<10}: [")  # format specifier for 'Tag    :  ['

        # present them with their results

        # print the lotto numbers
        print(prefs.format("Lotto"), end='')
        for i in range(len(lotto)):
            print(formats.format(lotto[i]), end='')
        print(" ]")

        # print their numbers
        print(prefs.format("Guesses"), end='')
        for i in range(len(guesses)):
            print(formats.format(guesses[i]), end='')
        print(" ]")

        # print which are correct
        print(prefs.format("Matches"), end='')
        for i in range(len(matches)):
            print(formats.format(__sd[matches[i]]), end='')
            if(matches[i]):
                correct += 1
        print(" ]\n\n")

        if correct >= n:
            print("Congratulations! You win $0!")
        else:
            print(f"Darn! Only {n-correct} left!")

        print(f"Continue? ({__cont}/n)")
        inp = input(" > ")

    print("Bye!")

    print(__info__)


__main__()
