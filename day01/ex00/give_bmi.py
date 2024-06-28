import numpy as np


def check_list(height: list[int | float], weight: list[int | float]) -> bool:
    """check_list is a fonction that check the list given by the user"""

    if len(height) == 0 or len(weight) == 0:
        print("\033[0;31mError: one of the list is empty\033[0m")
        return True

    for i in height:
        if isinstance(i, int) is False and isinstance(i, float) is False:
            print("\033[0;31mError: argument is not\
 a list of integer or float\033[0m")
            return True
        if i <= 0:
            print("\033[0;31mError: wrong value enter\033[0m")
            return True

    for i in weight:
        if isinstance(i, int) is False and isinstance(i, float) is False:
            print("\033[0;31mError: argument is not\
 a list of integer or float\033[0m")
            return True
        if i <= 0:
            print("\033[0;31mError: wrong value enter\033[0m")
            return True

    if len(height) != len(weight):
        print("\033[0;31mError: list in argument are not the same size\033[0m")
        return True
    return False


def calcul_bmi(a: any, b: any) -> float:
    """this fonction take two int or float and return the bmi"""

    return (a / (b * b))


def give_bmi(H: list[int | float], W: list[int | float]) -> list[int | float]:
    """this fonction take two list and allocate a new list with
the result of the two list given"""

    if check_list(H, W) is True:
        return None
    h = np.array([H, W])

    i = 0
    while i < len(H):
        h[0][i] = calcul_bmi(h[1][i], h[0][i])
        i += 1
    bmi = list(h[0])
    return (bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit, accepts a list of integers or
floats and an integer representing
a limit as parameters. It returns a list of booleans"""

    if bmi is None:
        print("\033[0;31mError: bmi given is None\033[0m")
        return
    elif isinstance(limit, int) is False:
        print("\033[0;31mError: limit given is not a int\033[0m")
        return

    i = 0
    list_limit = list(bmi)

    while i < len(bmi):
        if bmi[i] >= limit:
            list_limit[i] = True
        else:
            list_limit[i] = False
        i += 1
    return list_limit


def main():
    height = [2.71, 1.15, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    if bmi is None:
        print("None was return")

    height = [2.71, 1.15, "test"]
    weight = [165.3, 38.4, 1]

    bmi = give_bmi(height, weight)
    if bmi is None:
        print("None was return")

    height = []
    weight = []

    bmi = give_bmi(height, weight)
    if bmi is None:
        print("None was return")
    print(apply_limit(bmi, 26))
    return


if __name__ == "__main__":
    main()
