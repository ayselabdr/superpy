# Imports
import argparse
import csv
from datetime import date, datetime, timedelta

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

# Function to move date further by the amount of days
def advance_date(days):
    new_date=get_date()+timedelta(days=days)
    date_file=open('./date', 'w')
    date_file.write(datetime.strftime(new_date, '%Y-%m-%d'))
    date_file.close()
    return(get_date())

# Function to reset date to today
def reset_date():
    date_file=open('./date', 'w')
    date_file.write(datetime.strftime(datetime.now(), '%Y-%m-%d'))
    date_file.close()
    return(get_date())


# Function to buy an item and place it into our stock.
# Adds values to the file stock.csv
def buy(product_name, buy_price, expiration_date):
    with open("./stock.csv", mode='a') as stock:
        stock_writer=csv.writer(stock, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        stock_writer.writerow([product_name, datetime.strftime(get_date(), '%Y-%m-%d'), buy_price, expiration_date])
    return(print("Product added to the stock, nice."))



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


# Function to calculate revenue based on date or month or year
# Accepts date in formats like YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow
def report_revenue(daterange):
    if daterange.lower()=="today":
        datetime.strftime(get_date(), '%Y-%m-%d')
    if daterange.lower()=="yesterday":
        datetime.strftime(get_date()-timedelta(days=1), '%Y-%m-%d')
    if daterange.lower()=="tomorrow":
        datetime.strftime(get_date()+timedelta(days=1), '%Y-%m-%d')
    daterange=str(daterange)
    if len(daterange)>4:
        dates=daterange.split('-')
    else:
        dates=[daterange]
    import calendar
    if len(dates)==1:
        start_date=datetime.strptime(dates[0]+'-01-01', '%Y-%m-%d')
        end_date=datetime.strptime(dates[0]+'-12-31', '%Y-%m-%d')
    elif len(dates)==2:
        start_date=datetime.strptime(f'{daterange}-01', '%Y-%m-%d')
        end_date=datetime.strptime(f'{daterange}-{calendar.monthrange(int(dates[0]), int(dates[1]))[1]}', '%Y-%m-%d')
    elif len(dates)==3:
        start_date=datetime.strptime(f'{dates[0]}-{dates[1]}-{dates[2]}', '%Y-%m-%d')-timedelta(days=1)
        end_date=datetime.strptime(f'{dates[0]}-{dates[1]}-{dates[2]}', '%Y-%m-%d')+timedelta(days=1)
    else:
        print("Give me a date like 2023-12-12, or 2023-12, or at least a year like 2023")
    with open('sold.csv', 'r') as sold:
        sold_reader=csv.reader(sold)
        list_sold=list(sold_reader)
    revenue_total=0
    counter=0
    for sold_items in list_sold:
        if datetime.strptime(sold_items[1], '%Y-%m-%d')>start_date and datetime.strptime(sold_items[1], '%Y-%m-%d')<end_date:
            revenue_total+=int(sold_items[2])
        else:
            counter+=1
    if counter==len(list_sold):
        print("No revenue in that date range!")
    else:
        return(revenue_total)

# Function to calculate profit based on date or month or year
# Accepts date in formats like YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow
def report_profit(daterange):
    if daterange.lower()=="today":
        datetime.strftime(get_date(), '%Y-%m-%d')
    if daterange.lower()=="yesterday":
        datetime.strftime(get_date()-timedelta(days=1), '%Y-%m-%d')
    if daterange.lower()=="tomorrow":
        datetime.strftime(get_date()+timedelta(days=1), '%Y-%m-%d')
    daterange=str(daterange)
    if len(daterange)>4:
        dates=daterange.split('-')
    else:
        dates=[daterange]
    import calendar
    if len(dates)==1:
        start_date=datetime.strptime(dates[0]+'-01-01', '%Y-%m-%d')
        end_date=datetime.strptime(dates[0]+'-12-31', '%Y-%m-%d')
    elif len(dates)==2:
        start_date=datetime.strptime(f'{daterange}-01', '%Y-%m-%d')
        end_date=datetime.strptime(f'{daterange}-{calendar.monthrange(int(dates[0]), int(dates[1]))[1]}', '%Y-%m-%d')
    elif len(dates)==3:
        start_date=datetime.strptime(f'{dates[0]}-{dates[1]}-{dates[2]}', '%Y-%m-%d')-timedelta(days=1)
        end_date=datetime.strptime(f'{dates[0]}-{dates[1]}-{dates[2]}', '%Y-%m-%d')+timedelta(days=1)
    else:
        print("Give me a date like 2023-12-12, or 2023-12, or at least a year like 2023")
    with open('sold.csv', 'r') as sold:
        sold_reader=csv.reader(sold)
        list_sold=list(sold_reader)
    with open('stock.csv', 'r') as stock:
        stock_reader=csv.reader(stock)
        list_stock=list(stock_reader)
    revenue_total=0
    original_price_total=0
    counter=0
    for sold_items in list_sold:
        if datetime.strptime(sold_items[1], '%Y-%m-%d')>start_date and datetime.strptime(sold_items[1], '%Y-%m-%d')<end_date:
            revenue_total+=int(sold_items[2])
            original_price_total+=int(sold_items[3])
        else:
            counter+=1
    if counter==len(list_sold):
        print("No profit in that date range!")
    else:
        return(revenue_total-original_price_total)



# Function to sell the item
# Check the inventory, if item is available, sells
# Add sold item info to sold.csv
# For the sake of convinience, we assume we can only sell the item next day after it was bought
# And all prices are int, just because
def sell(product_name, sell_price):
    parser = argparse.ArgumentParser(description='Welcome to SuperPy!')

    subparsers = parser.add_subparsers(dest='command')

    buy_parser = subparsers.add_parser('buy', help='Buy a product')
    buy_parser.add_argument('--product_name', help='Name of the product')
    buy_parser.add_argument('--buy_price', type=int, help='Price of the product')
    buy_parser.add_argument('--expiration_date', help='Expiration date of the product')

    sell_parser = subparsers.add_parser('sell', help='Sell a product')
    sell_parser.add_argument('--product_name', help='Name of the product')
    sell_parser.add_argument('--sell_price', type=int, help='Price for selling the product')

    inventory_parser = subparsers.add_parser('inventory', help='List current inventory for today')

    profit_parser = subparsers.add_parser('profit', help='Calculate profit')
    profit_parser.add_argument('--date', help='Specify date or date range (YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow)')

    revenue_parser = subparsers.add_parser('revenue', help='Calculate revenue')
    revenue_parser.add_argument('--date', help='Specify date or date range (YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow)')

    get_date_parser = subparsers.add_parser('today', help='Get "today" date from date file')

    advance_date_parser = subparsers.add_parser('advance_date', help='Advance date by specified days')
    advance_date_parser.add_argument('--days', type=int, help='Number of days to advance the date')

    reset_date_parser = subparsers.add_parser('reset_date', help='Reset date to the actual today')

    args = parser.parse_args()

    if args.command == 'buy':
        if args.product_name and args.buy_price and args.expiration_date:
            buy(args.product_name, args.buy_price, args.expiration_date)
        else:
            print("Please provide all options for buying: --product_name, --buy_price, --expiration_date")
    elif args.command == 'sell':
        if args.product_name and args.sell_price:
            sell(args.product_name, args.sell_price)
        else:
            print("Please provide all options for selling: --product_name, --sell_price")
    elif args.command == 'inventory':
        list_inventory()
    elif args.command == 'profit':
        if args.date:
            report_profit(args.date)
        else:
            print("Please provide a date or date range for profit reporting")
    elif args.command == 'revenue':
        if args.date:
            report_revenue(args.date)
        else:
            print("Please provide a date or date range for revenue reporting")
    elif args.command == 'today':
        get_date()
    elif args.command == 'advance_date':
        if args.days:
            advance_date(args.days)
        else:
            print("Please provide the number of days to advance")
    elif args.command == 'reset_date':
        reset_date()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
