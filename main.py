# Imports
import argparse
import csv
from datetime import date, datetime, timedelta

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
from rich import print
from date_functions import *
from reporting_functions import *
from buy_sell_functions import *



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
