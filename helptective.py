# -*- coding: utf-8 -*-

from ChuckData import *

SPENT = STORE_NAME = HOURS = 0
TIME = CATALOG = MINUTES = 1
ERROR_MARGIN = 0.001

routes = []
test = []
solution = 1

def guess_routes(ticket=0):
    global solution
    tickets = len(purchasesList)
    stores = len(catalogList)
    print("ticket is", ticket)
    if ticket == tickets:
        print_results(solution, routes)
    else:
        paid_price = purchasesList[ticket][SPENT]
        print(paid_price)
        for store in range(stores):
            print("3 veces")
            print(store)
            if valid_purchase(paid_price, store)\
               and (valid_time(ticket, store)):
                print("went in")
                generate_purchases_combis(paid_price, store)
                routes.append((catalogList[store][STORE_NAME],
                               test))
        guess_routes(ticket + 1)



def valid_purchase(paid_price, store):
    """asdf
    """
    store_size = len(catalogList[store][CATALOG].values())
    price_of_items = list(catalogList[store][CATALOG].values())

    if -ERROR_MARGIN < paid_price < ERROR_MARGIN:
        return True
    elif paid_price < -ERROR_MARGIN:
        return False
    else:
        i = 0
        while i < store_size:
            if valid_purchase(paid_price - price_of_items[i], store):
                return True
            i += 1
        return False


def init_possible_purchases(store):
    catalog = catalogList[store][CATALOG]
    possible_purchases = dict(catalog)
    for item in possible_purchases:
        possible_purchases[item] = 0
    return possible_purchases


def generate_purchases_combis(paid_price, store, possible_purchases=None):
    """asdf
    """

    catalog = catalogList[store][CATALOG]
    #    print(price_of_items)

    if possible_purchases is None:
        possible_purchases = init_possible_purchases(store)
    if -ERROR_MARGIN < paid_price < ERROR_MARGIN:
        return True
    elif paid_price < -ERROR_MARGIN:
        return False
    else:
        for item in catalog:
            price_of_item = catalog[item]
            possible_purchases[item] += 1
            if generate_purchases_combis(paid_price - price_of_item,
                                         store,
                                         possible_purchases):
                if possible_purchases not in test:
                    test.append(dict(possible_purchases))
            possible_purchases[item] -= 1
    return False                # Arreglar lo de los returns y las variables


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
    print(minutes)

    return minutes


def valid_time(ticket, store):
    if ticket == 0:
        return True
    else:
        on_the_road = calc_time(purchasesList[ticket - 1][TIME],
                                purchasesList[ticket][TIME])
        print(storesDistance[store])
        if on_the_road in storesDistance[store]:
            print("ASDFASDFASDFASD")
            return True
        else:
            return False


def print_results(solution, routes):
    print("Solution number", solution)
    print("------------------------------ #")
    for elem in routes:
        for elem2 in elem:
            if elem.index(elem2) == 1:
                for elem3 in elem2:
                    print(elem3)
    print()
    print()


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



def main():
    sort_purchaseList(purchasesList, 0, len(purchasesList) - 1)
    guess_routes()

if __name__ == '__main__':
    main()
