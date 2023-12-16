# Imports
import argparse
import csv
from datetime import date, datetime, timedelta

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
from rich import print

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
    new_stock=[]
    for sold_item in list_sold:
        for stock_item in list_stock:
            if sold_item[0]==stock_item[0]:
                if (datetime.strptime(sold_item[1], '%Y-%m-%d')>datetime.strptime(stock_item[3], '%Y-%m-%d') and
                datetime.strptime(sold_item[1], '%Y-%m-%d')<datetime.strptime(stock_item[1], '%Y-%m-%d') and
                datetime.strptime(sold_item[1], '%Y-%m-%d')>get_date()):
                    new_stock.append(stock_item)
    for stock_item in list_stock:
        if (get_date()>datetime.strptime(stock_item[1], '%Y-%m-%d') and get_date()<datetime.strptime(stock_item[3], '%Y-%m-%d')):
            new_stock.append(stock_item)
    print(len(new_stock))
    if len(new_stock)>0:
        with open("./reports_log.csv", mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "inventory", new_stock])
    else:    
        with open("./reports_log.csv", mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "inventory", "It is empty"])
    return(new_stock)


# Function to calculate revenue based on date or month or year
# Accepts date in formats like YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow
def report_revenue(daterange):
    if daterange.lower()=="today":
        daterange=datetime.strftime(get_date(), '%Y-%m-%d')
    if daterange.lower()=="yesterday":
        daterange=datetime.strftime(get_date()-timedelta(days=1), '%Y-%m-%d')
    if daterange.lower()=="tomorrow":
        daterange=datetime.strftime(get_date()+timedelta(days=1), '%Y-%m-%d')
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
        with open("./reports_log.csv", mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "revenue", f"Requested for: {daterange} - No revenue :( )"])
        print("No revenue in that date range!")
    else:
        with open("./reports_log.csv", mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "revenue", f"Requested for: {daterange} - revenue is {revenue_total}"])
        return(revenue_total)

# Function to calculate profit based on date or month or year
# Accepts date in formats like YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow
def report_profit(daterange):
    if daterange.lower()=="today":
        daterange=datetime.strftime(get_date(), '%Y-%m-%d')
    if daterange.lower()=="yesterday":
        daterange=datetime.strftime(get_date()-timedelta(days=1), '%Y-%m-%d')
    if daterange.lower()=="tomorrow":
        daterange=datetime.strftime(get_date()+timedelta(days=1), '%Y-%m-%d')
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
        with open("./reports_log.csv", mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "profits", f"Requested for: {daterange} - No profits :( )"])
        print("No profit in that date range!")
    else:
        with open("./reports_log.csv", mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "profits", f"Requested for: {daterange} - profit is {revenue_total-original_price_total}"])
        return(revenue_total-original_price_total)



# Function to sell the item
# Check the inventory, if item is available, sells
# Add sold item info to sold.csv
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
                sold_writer.writerow([product_name, datetime.strftime(get_date(), '%Y-%m-%d'), sell_price, items[2]])
            print(f'One {product_name} sold!')
            break
    if counter==0:
        print("Out of stock, buddy")



def main():
    parser = argparse.ArgumentParser(description='Welcome to SuperPy!')

    subparsers = parser.add_subparsers(dest='base_command')

    # Subparser for buy command
    buy_parser = subparsers.add_parser('buy', help='Buy a product')
    buy_parser.add_argument('--product_name', help='Name of the product')
    buy_parser.add_argument('--buy_price', type=int, help='Price of the product')
    buy_parser.add_argument('--expiration_date', help='Expiration date of the product')

    # Subparser for sell command
    sell_parser = subparsers.add_parser('sell', help='Sell a product')
    sell_parser.add_argument('--product_name', help='Name of the product')
    sell_parser.add_argument('--sell_price', type=int, help='Price for selling the product')

    # Subparser for report command
    report_parser = subparsers.add_parser('report', help='Generate reports')

    # Subparsers for report command (inventory, profit, revenue)
    report_subparsers = report_parser.add_subparsers(dest='report_command')

    inventory_parser = report_subparsers.add_parser('inventory', help='List current inventory')

    profit_parser = report_subparsers.add_parser('profit', help='Calculate profit')
    profit_parser.add_argument('--date', help='Specify date or date range (YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow)')

    revenue_parser = report_subparsers.add_parser('revenue', help='Calculate revenue')
    revenue_parser.add_argument('--date', help='Specify date or date range (YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow)')

    # Subparsers for date commands
    date_parser = subparsers.add_parser('date', help='Operations related to date')

    date_subparsers = date_parser.add_subparsers(dest='date_command')

    get_date_parser = date_subparsers.add_parser('today', help='Get date from date file')

    advance_date_parser = date_subparsers.add_parser('advance_date', help='Advance date by specified days')
    advance_date_parser.add_argument('--days', type=int, help='Number of days to advance the date')

    reset_date_parser = date_subparsers.add_parser('reset_date', help='Reset date to today')

    args = parser.parse_args()

    if args.base_command == 'buy':
        if args.product_name and args.buy_price and args.expiration_date:
            buy(args.product_name, args.buy_price, args.expiration_date)
        else:
            print("[bold red]Please provide all options for buying: --product_name, --buy_price, --expiration_date[/bold red]")
    elif args.base_command == 'sell':
        if args.product_name and args.sell_price:
            sell(args.product_name, args.sell_price)
        else:
            print("[bold red]Please provide all options for selling: --product_name, --sell_price[/bold red]")
    elif args.base_command == 'report':
        if args.report_command == 'inventory':
            print("[bold green][Product_name, Purchase_date, Price, Expiry_date][/bold green]")
            for i in list_inventory():
                print(f'[blue]{i}[/blue]')
        elif args.report_command == 'profit':
            if args.date:
                print(f'[bold blue]{report_profit(args.date)}[/bold blue]')
            else:
                print("[bold red]Please provide a date or date range for profit reporting[/bold red]")
        elif args.report_command == 'revenue':
            if args.date:
                print(f'[bold blue]{report_revenue(args.date)}[/bold blue]')
            else:
                print("[bold red]Please provide a date or date range for revenue reporting[/bold red]")
        else:
            report_parser.print_help()
    elif args.base_command == 'date':
        if args.date_command == 'today':
            print(f"[bold blue]We assume that today is {datetime.strftime(get_date(), '%Y-%m-%d')}.[bold blue]")
        elif args.date_command == 'advance_date':
            if args.days:
                advance_date(args.days)
                print(f"[bold blue]It is now {datetime.strftime(get_date(), '%Y-%m-%d')}, hope you are happy.[bold blue]")
            else:
                print("[bold red]Please provide the number of days to advance[/bold red]")
        elif args.date_command == 'reset_date':
            reset_date()
            print(f"[bold blue]We are back to {datetime.strftime(get_date(), '%Y-%m-%d')}.[bold blue]")
        else:
            date_parser.print_help()
    else:
        parser.print_help()

import json
csvfile = open('reports_log.csv', 'r')
jsonfile = open('report_log_json.json', 'w')

fieldnames = ("DateOfReport", "ActualDateOfReport", "TypeOfReport", "Result")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, sort_keys=False, indent=4, separators=(',', ': '))
    jsonfile.write('\n')

if __name__ == "__main__":
    main()
