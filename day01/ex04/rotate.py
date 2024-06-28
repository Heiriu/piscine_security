from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def print_transpose_size(row: int, cow: int, new_list: np):
    """display the data of an image after transpose"""

    print("\033[0;33mNew shape after transpose:\
\033[0m (", row, ", ", cow, ")", sep="")
    print(new_list)


def transpose(img: np):
    """rotate an img and display it"""

    rotate = [[img[j][i] for j in range(len(img))] for i in range(len(img[0]))]

    new_list = [[]]
    i = 0
    while i < len(rotate):
        y = 0
        while y < len(rotate):
            new_list[0].append(list(rotate[i][y]))
            y += 1
        i += 1
    new_list = np.array(new_list)
    print_transpose_size(len(rotate), len(rotate[0]), new_list)

    plt.imshow(rotate, cmap="gray")
    plt.show()


def main():
    img = ft_load("animal.jpeg")
    if img is None:
        return
    transpose(img)


if __name__ == "__main__":
    main()
