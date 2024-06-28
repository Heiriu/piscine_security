import numpy as np
import cv2


def print_new_size(row: int, cow: int, image: np, list_img: np):
    """display the information of an image after zooming"""

    print("\033[0;33mNew shape after slicing:\
\033[0m ", image.shape, " or (", row, ", ", cow, ")", sep="")
    print(list_img)


def ft_load(path: str) -> np:
    """is a fonction that load an image,prints its format
and its pixels content in RGB format"""

    image = cv2.imread(path)
    if image is None:
        print("\033[0;31mError: cannot open the file\033[0m")
        return (None)

    for i in image:
        for y in i:
            first = y[0]
            y[0] = y[2]
            y[2] = first
    image = zoom_img(image)
    return (image)


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
    return slice_image


def main():
    return


if __name__ == "__main__":
    main()
