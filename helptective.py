# -*- coding: utf-8 -*-

from ChuckData import *

SPENT = STORE_NAME = HOURS = 0
TIME = CATALOG = MINUTES = 1

routes = []


def guess_routes(store=0):
    print(calc_time([17, 40], [16, 40]))
    print(purchasesList)


def calc_time(time1, time2):
    """
    Returns an integer (minutes difference)

    """

    hours = time2[HOURS] - time1[HOURS]
    minutes = (time2[MINUTES] - time1[MINUTES])
    if minutes < 0:
        hours -= 1
    minutes %= 60
    minutes += hours * 60

    return minutes


def check_purchases():
    print(catalogList)


def print_results():
    pass


def main():
    guess_routes()


if __name__ == '__main__':
    main()
