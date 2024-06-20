import requests
import sys
import os
from bs4 import BeautifulSoup
import urllib.request


def download_image(url, file_path, file_name):
    full_path = file_path + file_name
    try:
        urllib.request.urlretrieve(url, full_path)
        print("\033[0;32mImage download sucessfuly at:\033[0m", full_path)
    except ValueError:
        url = "http:" + url
        try:
            urllib.request.urlretrieve(url, full_path)
        except ValueError as e:
           sys.exit(e)



def recursive_download(list_img: list, option: dict, i: int):
    split = list_img[i].split(".")
    file_name = 'img' + str(i) + '.' + split[len(split) - 1]
    download_image(list_img[i], option['p'], file_name)
    i += 1
    if i < len(list_img) and option['l'] > 0:
        if i < option['l']:
            recursive_download(list_img, option, i)
    elif i < len(list_img):
        recursive_download(list_img, option, i)


def getdata(url: str):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return r.text


def scrap_img(string: str, option: dict):
    if option['p'] != "":
        try:  
            os.mkdir(option['p'])  
        except OSError:  
            pass

    htmldata = getdata(string[len(string) - 1])
    soup = BeautifulSoup(htmldata, 'html.parser')
    list_img = []
    for item in soup.find_all('img'):
        list_img.append(item['src'])
    recursive_download(list_img, option, 0)


def check_flags(flags: str, option: dict) -> list:
    for i in flags:
        y = 0
        while len(i) > y:
            if i[y] == '-':
                y += 1
                while len(i) > y:
                    if i[y] == 'r':
                        option['r'] = 1
                    elif i[y] == 'l':
                        option['l'] = 5
                    elif i[y] == 'p':
                        option['p'] = "./data/"
                    else:
                        print("\033[0;31mError: wrong flag used\033[0m")
                        sys.exit()
                    y += 1
            elif i[y] >= '0' and i[y] <= '9':
                option['l'] = int(i)
                y = len(i)
            elif option['p'] == "./data/":
                option['p'] = i
                y = len(i)
            else:
                print("\033[0;31mError: wrong argument provided\033[0m")
                sys.exit()
            y += 1
    return option


def main():
    if len(sys.argv) <= 1:
        print("\033[0;31mError: missing arg or too many arg\033[0m")
        return
    option = {"r": 0, "l": 0, "p": ""}
    if len(sys.argv) > 2:
        option = check_flags(sys.argv[1:len(sys.argv) - 1], option)
    scrap_img(sys.argv, option)


if __name__ == "__main__":
    main()
