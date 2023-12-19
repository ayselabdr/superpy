# **Welcome to SuperPy!**

Let's take a look over the functionality of this project and how to use it.

## Table of contents

1. [Date Functions](#datefunctions)</br>
    1.1 [Today](#today)</br>
    1.2 [Advance date](#advancedate)</br>
    1.3 [Reset date](#resetdate)
2. [Buy and Sell]</br>
    2.1 [Buy]</br>
    2.2 [Sell]
3. [Reporting]</br>
    3.1 [List inventory]</br>
    3.2 [Report revenue]</br>
    3.3 [Report profits]</br>
    3.3 [Reporting files]



## Date Functions <a name="datefunctions"></a> 

All date related functions can be found in the `date_functions.py` file.

### Today <a name="today"></a></br>
A function to fetch the assumed today's date - date that is stored in the file `./date`. Date is always stored in YYYY-MM-DD format (across the whole project too btw). Use it as below:</br>
`python3 main.py date today` </br>
Which should give you a result like: </br>
`We assume that today is 2024-01-07.`

### Advance date <a name="advancedate"></a></br>
A function to move the assumed today's date further in the future - will update the date that is stored in the file `./date`. Takes an option `--days` which accepts an integer - a number of days to move forward. Use it as below:</br>
`python3 main.py date advance_date --days 2` </br>
Which should give you a result like: </br>
`It is now 2024-01-09, hope you are happy.`

### Reset date <a name="resetdate"></a></br>
A function to reset asuumed today's date to actual real life today's date. As you may have guessed, it will write to `./date` file. Use it as below:</br>
`python3 main.py date reset_date` </br>
Which should give you a result like: </br>
`We are back to 2023-12-19.`