from datetime import datetime
from time import sleep


# Part 1
def clock(n: int) -> str:
    """
    returns the current time for n seconds

    Parameters
    ----------
    n: int
        number of seconds the function will run for
    """
    # Your code here
    for i in range(n):
        x = datetime.now()
        time = x.strftime("%H:%M:%S")
        print(f"{time}", end="\r")
        sleep(1)



# Part 2
def lcm(a: int, b: int) -> int:
    """
    returns the lowest common multiple of a and b

    Parameters
    ----------
    a: int
        first number
    b: int:
        second number
    """
    # Your code here
    done = False
    a_og = a
    b_og = b
    while done is False:
        if a == b:
            lcm = a
            done = True
        elif a > b:
            b += b_og
        elif b > a:
            a += a_og
    return lcm


# Part 3
def gcf(a: int, b: int) -> int:
    """
    returns the greatest common factor of a and b

    Parameters
    ----------
    a: int
    first number

    b: int
    second number
    """
    # Your code here\
    done = False
    while done is False:
        if b == 0:
            gcf = a
            done = True
        else:
            remainder = a % b
            a = b
            b = remainder
    return gcf


