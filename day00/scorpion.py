from PIL import Image
from PIL.ExifTags import TAGS
import sys


def extract_metadata(imagename: str):
    try:
        image = Image.open(imagename)

        info_dict = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }
        
        for label,value in info_dict.items():
            print(f"\033[0;34m{label:25}:\033[0m \033[0;33m{value}\033[0m")
        print()

    except FileNotFoundError:
        sys.exit(f"\033[0;31mError: file {imagename} not found, skipping\033[0m")


def main():
    if len(sys.argv) <= 1:
        sys.exit("\033[0;31mError: missing arg\033[0m")
    i = 1
    while i < len(sys.argv):
        extract_metadata(sys.argv[i])
        i += 1


if __name__ == "__main__":
    main()