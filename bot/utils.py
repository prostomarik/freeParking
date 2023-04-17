import cv2.cv2 as cv2
import requests
import telebot


def showImage(good, bad):  # список по 4 координаты свободных и занятых мест, формат : [x1, y1, x2, y2]
    image = cv2.imread('/home/vasily/PycharmProjects/freeParking/bot/bot.jpg')

    for tmp in good:
        image = cv2.rectangle(image, (tmp[0], tmp[1]), (tmp[2], tmp[3]), (0, 255, 0), 2)
    for tmp in bad:
        image = cv2.rectangle(image, (tmp[0], tmp[1]), (tmp[2], tmp[3]), (0, 0, 255), 2)
    # cv2.imshow('a', image)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return image


def update(link):
    r = requests.get(link, verify=False).text
    return r


def load_exchange(URL):
    return requests.get(URL, verify=False).text
