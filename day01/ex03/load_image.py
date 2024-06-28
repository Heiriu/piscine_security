import numpy as np
import cv2


def ft_load(path: str) -> np:
    """is a fonction that load an image,prints its format
and its pixels content in RGB format"""

    image = cv2.imread(path)
    if image is None:
        print("\033[0;31mError: cannot open the file\033[0m")
        return (None)

    new_list = [[]]
    for i in image:
        for y in i:
            first = y[0]
            y[0] = y[2]
            y[2] = first
    i = 0
    while i < len(image):
        y = 0
        while y < len(image[i]):
            new_list[0].append(list(image[i][y]))
            y += 1
        i += 1
    new_list = np.array(new_list)
    print("\033[0;33mThe shape of image is:\033[0m ", image.shape)
    print(new_list)
    return (image)


def main():
    print(ft_load("landscape.jp"))
    return


if __name__ == "__main__":
    main()
