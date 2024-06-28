from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def print_new_size(row: int, cow: int, image: np, list_img: np):
    """display the information of an image after zooming"""

    print("\033[0;33mNew shape after slicing:\
\033[0m ", image.shape, " or (", row, ", ", cow, ")", sep="")
    print(list_img)


def zoom_img(image: np):
    """zoom_img receive a np array from a jpg or a jpeg
and display it after zooming"""

    slice_image = image[100:500, 450:850, 0:1]

    (row, col) = slice_image.shape[0:2]
    new_list = [[]]
    i = 0
    while i < len(slice_image):
        y = 0
        while y < len(slice_image):
            new_list[0].append(list(slice_image[i][y]))
            y += 1
        i += 1
    new_list = np.array(new_list)
    print_new_size(row, col, slice_image, new_list)
    plt.imshow(slice_image, cmap="gray")
    plt.show()


def main():
    image = ft_load("animal.jpeg")
    if image is None:
        return
    zoom_img(image)


if __name__ == "__main__":
    main()
