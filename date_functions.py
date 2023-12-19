import argparse
import csv
from datetime import date, datetime, timedelta



def get_date():
    '''
    Function to get the date from our date file
    Parses ./date file for "current" date
    Returns a datetime object
    '''
    date_file=open('./date', 'r')
    date_read=date_file.read()
    today_date=datetime.strptime(date_read, '%Y-%m-%d')
    date_file.close()
    return(today_date)



def advance_date(days):
    '''
    Function to move date further by the amount of days
    '''
    new_date=get_date()+timedelta(days=days)
    date_file=open('./date', 'w')
    date_file.write(datetime.strftime(new_date, '%Y-%m-%d'))
    date_file.close()
    return(get_date())


def reset_date():
    '''
    Function to reset the date to actual today
    '''
    date_file=open('./date', 'w')
    date_file.write(datetime.strftime(datetime.now(), '%Y-%m-%d'))
    date_file.close()
    return(get_date())
