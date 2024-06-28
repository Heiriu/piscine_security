import numpy as np


def check_arg(family: list, start: int, end: int) -> bool:
    """is a fonction that check all the arg given by the user"""

    if isinstance(family, list) is False:
        print("\033[0;31mError: argument is not\
 a list of integer or float\033[0m")
        return False

    if len(family) == 0:
        print("\033[0;31mError: list is empty\033[0m")
        return False
    elif len(family[0]) == 0:
        print("\033[0;31mError: list is empty\033[0m")
        return False

    lenght = len(family[0])
    for i in family:
        if len(i) != lenght:
            print("\033[0;31mError: list is not\
 the same size\033[0m")
            return False

#    for i in family:
#        for y in i:
#            if isinstance(y, int) is False and isinstance(y, float) is False:
#                print("\033[0;31mError: argument is not\
# a list of integer or float\033[0m")
#                return False

    if isinstance(start, int) is False:
        print("\033[0;31mError: wrong type of argument\033[0m")
        return False

    if isinstance(end, int) is False:
        print("\033[0;31mError: wrong type of argument\033[0m")
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """this fonction take a 2D array, print is shape, and return a truncated
version of the array based on the provided start and end arguments"""

    if check_arg(family, start, end) is False:
        return
    print("\033[0;33mmy shape is :\033[0m\
 (", len(family), ", ", len(family[0]), ")", sep="")

    cpy = np.array(family)
    list_slice = slice(start, end, 1)
    cpy = cpy[list_slice]
    new_list = []
    for i in cpy:
        new_list.append(list(i))
    str = "\033[0;33mmy new shape is :\033[0m ("
    print(str, len(cpy), ", ", len(family[0]), ")", sep="")
    return (new_list)


def main():
    family = [[1.80, 78.4],
              [2.15, "str"],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))

    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2, 1]]
    print(slice_me(family, 0, 2))

    family = []
    print(slice_me(family, 0, 2))

    family = "1.80"
    print(slice_me(family, 0, 2))

    family = [[],
              [],
              [],
              []]
    print(slice_me(family, 0, 2))
    return


if __name__ == "__main__":
    main()
