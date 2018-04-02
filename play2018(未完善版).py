# 未完善项目：自动化2048
# 缺陷：很难得到高分
# 改善：需学习一定的相关算法

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random

def cName(x):
    return "tile.tile-" + str(x) + ".tile-position-" + str(column) + "-" + str(row)

def change():
    for a in range(3, 0, -1):
        for b in range(3, 0, -1):
            if num[a][b] == num[a - 1][b - 1]:
                if isinstance(num[a][b - 1], str):
                    print(1)
                    return kElement.send_keys(Keys.LEFT + Keys.UP)

    for a in range(3, 0, -1):
        for b in range(3):
            if num[a][b] == num[a - 1][b + 1]:
                if isinstance(num[a][b + 1], str):
                    print(2)
                    return kElement.send_keys(Keys.RIGHT + Keys.UP)

def ranKey():
    key = random.randint(0, 3)
    if key == 1:
        print(3)
        return kElement.send_keys(Keys.LEFT)

    if key == 2:
        print(3)
        return kElement.send_keys(Keys.RIGHT)

    if key == 0:
        print(3)
        return kElement.send_keys(Keys.UP)

browser = webdriver.Firefox()
browser.get("http://2048.oubk.com/")
kElement = browser.find_element_by_tag_name("html")
num2 = [[], [], [], []]
ran = 0

for i in range(2000):
    exit_flag = False
    print(i)
    num = [["a", "b", "c", "d"], ["e", "f", "g", "h"], ["i", "j", "k", "l"], ["m", "n", "o", "p"]]
    for column in range(1, 5):
        for row in range(1, 5):
            for n in range(10):
                x = 2 ** n
                try:
                    conElement = browser.find_element_by_class_name("tile-container")
                    oldElement = conElement.find_element_by_class_name(str(cName(x)))
                except:
                    pass
                else:
                    numElement2 = oldElement.find_element_by_class_name("tile-inner")
                    num[row - 1][column - 1] = numElement2.text

    print(num)
    for m in range(4):
        for n in range(3, 0, -1):
            if num[n][m] == num[n - 1][m]:
                kElement.send_keys(Keys.UP)
                print(4)
                exit_flag = True
                break

            else:
                if isinstance(num[n - 1][m], str):
                    try:
                        if num[n][m] == num[n - 2][m]:
                            kElement.send_keys(Keys.UP)
                            print(4)
                            exit_flag = True
                            break
                        else:
                            if isinstance(num[n - 2][m], str):
                                if num[n][m] == num[n - 3][m]:
                                    kElement.send_keys(Keys.UP)
                                    print(4)
                                    exit_flag = True
                                    break
                    except:
                        pass

            if num[m][n] == num[m][n - 1]:
                kElement.send_keys(Keys.LEFT)
                print(5)
                exit_flag = True
                break

            else:
                if isinstance(num[m][n - 1], str):
                    try:
                        if num[m][n] == num[m][n - 2]:
                            kElement.send_keys(Keys.LEFT)
                            print(5)
                            exit_flag = True
                            break
                        else:
                            if isinstance(num[m][n - 2], str):
                                if num[m][n] == num[m][n - 3]:
                                    kElement.send_keys(Keys.LEFT)
                                    print(5)
                                    exit_flag = True
                                    break
                    except:
                        pass

    print(num2)
    print(num)
    if num2 != num:
        num2 = num
    else:
        change()
        ran += 1

    if ran > 1:
        ranKey()
        if ran > 5:
            kElement.send_keys(Keys.DOWN)
            print(6)
            ran = 0
