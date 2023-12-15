# Imports
import argparse
import csv
from datetime import date, datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# Function to get the date from our date file.
# Returns a datetime object.
def get_date():
    date_file=open('./date', 'r')
    date_read=date_file.read()
    today_date=datetime.strptime(date_read, '%Y-%m-%d')
    date_file.close()
    return(today_date)



# Function to buy an item and place it into our stock.
# Adds values to the file stock.csv
def buy(product_name, buy_price, expiration_date):
    with open("./stock.csv", mode='a') as stock:
        stock_writer=csv.writer(stock, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        stock_writer.writerow([product_name, datetime.strftime(get_date(), '%Y-%m-%d'), buy_price, expiration_date])



# Function to check current inventory
# Fetches current date, then compares two csv files
# Builds an updated inventory in a form of list of lists
def list_inventory():
    with open('stock.csv', 'r') as stock:
        stock_reader=csv.reader(stock)
        list_stock=list(stock_reader)
    with open('sold.csv', 'r') as sold:
        sold_reader=csv.reader(sold)
        list_sold=list(sold_reader)
    for sold_item in list_sold:
        for stock_item in list_stock:
            if sold_item[0]==stock_item[0]:
                if datetime.strptime(sold_item[1], '%Y-%m-%d')<datetime.strptime(stock_item[3], '%Y-%m-%d'):
                    if datetime.strptime(sold_item[1], '%Y-%m-%d')>=datetime.strptime(stock_item[1], '%Y-%m-%d'):
                        list_stock.remove(stock_item)
    for stock_item in list_stock:
        if get_date()>datetime.strptime(stock_item[3], '%Y-%m-%d'):
            list_stock.remove(stock_item)
    return(list_stock)


def report_revenue():
    with open('sold.csv', 'r') as sold:
        sold_reader=csv.reader(sold)
        list_sold=list(sold_reader)
    revenue_total=0
    for sold_items in list_sold:
        if datetime.strptime(sold_items[1], '%Y-%m-%d')<get_date():
            revenue_total+=int(sold_items[2])
    return(revenue_total)





# Function to sell the item
# Check the inventory, if item is available, sells
# Add sold item info to csv
# For the sake of convinience, we assume we can only sell the item next day after it was bought
# And all prices are int, just because
def sell(product_name, sell_price):
    for items in list_inventory():
        counter=0
        if (items[0]==product_name and 
        datetime.strptime(items[3], '%Y-%m-%d')>get_date() and 
        datetime.strptime(items[1], '%Y-%m-%d')<get_date() and 
        int(items[2])<sell_price):
            counter+=1
            with open("./sold.csv", mode="a") as sold:
                sold_writer=csv.writer(sold, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                sold_writer.writerow([product_name, datetime.strftime(get_date(), '%Y-%m-%d'), sell_price])
            print(f'one {product_name} sold!')
            break
    if counter==0:
        print("out of stock, buddy")





def main():
    pass


if __name__ == "__main__":
    main()
