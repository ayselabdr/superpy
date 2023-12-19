import csv
from datetime import date, datetime, timedelta
from date_functions import *


def list_inventory():
    '''
    Function to check current inventory
    Fetches current date, then compares two csv files
    Builds an updated inventory in a form of list of lists
    '''
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
    if len(new_stock)>0:
        with open("./reports_log.csv", newline='', mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "inventory", new_stock])
    else:    
        with open("./reports_log.csv", newline='', mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "inventory", "It is empty"])
    return(new_stock)



def report_revenue(daterange):
    '''
    Function to calculate revenue based on date or month or year
    Accepts date in formats like YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow
    '''
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
        with open("./reports_log.csv", newline='', mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "revenue", f"Requested for: {daterange} - No revenue :( )"])
        print("No revenue in that date range!")
    else:
        with open("./reports_log.csv", newline='', mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "revenue", f"Requested for: {daterange} - revenue is {revenue_total}"])
        return(revenue_total)



def report_profit(daterange):
    '''
    Function to calculate profit based on date or month or year
    Accepts date in formats like YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow
    '''
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
        with open("./reports_log.csv", newline='', mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "profits", f"Requested for: {daterange} - No profits :( )"])
        print("No profit in that date range!")
    else:
        with open("./reports_log.csv", newline='', mode="a") as reports:
            reports_writer=csv.writer(reports, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            reports_writer.writerow([datetime.strftime(get_date(), '%Y-%m-%d'), datetime.strftime(datetime.now(), '%Y-%m-%d'), "profits", f"Requested for: {daterange} - profit is {revenue_total-original_price_total}"])
        return(revenue_total-original_price_total)
