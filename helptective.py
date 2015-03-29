# -*- coding: utf-8 -*-

from ChuckData import *

SPENT = STORE_NAME = HOURS = 0
TIME = CATALOG = MINUTES  = 1

routes = []


def guess_routes(store=0):
    if check_purchases(store)


def split(purchases, start, end):
    """Choosing where to split the vector for quicksorting"""
    pivot = purchases[end]
    i = start - 1
    for j in range(start, end):
        time1 = purchases[j][TIME][HOURS] * 60 + purchases[j][TIME][MINUTES]
        time2 = pivot[TIME][HOURS] * 60 + pivot[TIME][MINUTES]
        if time1 <= time2:
            i += 1
            purchases[i], purchases[j] = purchases[j], purchases[i]
    purchases[i + 1], purchases[end] = purchases[end], purchases[i + 1]
    return i + 1


def sort_purchaseList(purchases, start, end):
    """Function to quicksort the purchase list chronologically

    """
    if start < end:
        partition = split(purchases, start, end)
        sort_purchaseList(purchases, start, partition - 1)
        sort_purchaseList(purchases, partition + 1, end)



def calc_time(time1, time2):
    """
    Keyword Arguments:
    time -- tuple containing a time

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
    sort_purchaseList(purchasesList, 0, len(purchasesList) - 1)
    guess_routes()




if __name__ == '__main__':
    main()
