# Imports
import argparse
import csv
from datetime import date, datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# CSV files
#inventory_file=open('./inventory.csv', 'r')
#sold_file=open('./sold.csv', 'r')

# Establish the date from the start
date_file=open('./date', 'r')
date_read=date_file.read()
today_date=datetime.strptime(date_read, '%Y-%m-%d')
date_file.close()



#--product_name --buy_date --buy_price --expiration_date

def buy(product_name, buy_date, buy_price, expiration_date):
    with open("./inventory.csv", mode='w') as inventory:
        inventory_writer=csv.writer(inventory, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        inventory_writer.writerow([product_name, buy_date, buy_price, expiration_date])



def main():
    pass


if __name__ == "__main__":
    main()
