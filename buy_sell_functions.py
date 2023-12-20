import csv
from datetime import date, datetime, timedelta
from date_functions import *
from reporting_functions import *


def buy(product_name, buy_price, expiration_date):
    '''
    Function to buy an item and place it into our stock.
    Adds values to the file stock.csv
    '''
    with open("./stock.csv", newline='', mode='a') as stock:
        stock_writer=csv.writer(stock, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        stock_writer.writerow([product_name, datetime.strftime(get_date(), '%Y-%m-%d'), buy_price, expiration_date])
    return(print("Product added to the stock, nice."))




def sell(product_name, sell_price):
    '''
    Function to sell the item
    Check the inventory, if item is available, sells
    Add sold item info to sold.csv
    For the sake of convinience, we assume we can only sell the item next day after it was bought
    And all prices are int, just because
    '''
    for items in list_inventory():
        counter=0
        if (items[0]==product_name and 
        datetime.strptime(items[3], '%Y-%m-%d')>get_date() and 
        datetime.strptime(items[1], '%Y-%m-%d')<get_date() and 
        int(items[2])<sell_price):
            counter+=1
            with open("./sold.csv", newline='', mode="a") as sold:
                sold_writer=csv.writer(sold, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                sold_writer.writerow([product_name, datetime.strftime(get_date(), '%Y-%m-%d'), sell_price, items[2]])
            print(f'One {product_name} sold!')
            break
    if counter==0:
        print("Out of stock, buddy")