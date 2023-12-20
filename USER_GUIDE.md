# **Welcome to SuperPy!**

Let's take a look over the functionality of this project and how to use it.

## Table of contents

1. [Date Functions](#datefunctions)</br>
    1.1 [Today](#today)</br>
    1.2 [Advance date](#advancedate)</br>
    1.3 [Reset date](#resetdate)
2. [Buy and Sell](#buysell)</br>
    2.1 [Buy](#buy)</br>
    2.2 [Sell](#sell)
3. [Reporting](#reporting)</br>
    3.1 [List inventory](#inventory)</br>
    3.2 [Report revenue](#revenue)</br>
    3.3 [Report profits](#profit)</br>
    3.3 [Reporting files](#rep-files)


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



## Buy and Sell <a name="buysell"></a> 

Both buy and sell functions can be found in the `buy_sell_functions.py` file.

### Buy <a name="buy"></a>
A function to buy an item into our stock. It takes 3 options:</br>
`--product_name` - to name a product</br>
`--buy_price` - price at which we bought it</br>
`--expiration_date` - a date at which the product will expire</br>
Stock is logged in a `stock.csv` file. Columns are:[ProductName,BoughtDate,BoughtPrice,ExpirationDate].</br>
Use it as below:</br>
`python3 main.py buy --product_name parrot --buy_price 5 --expiration_date 2024-01-25` </br>
Which should give you a result like: </br>
`Product added to the stock, nice.`</br>
***Important note:*** Sometimes after something is bought, changes may not reflect in VSCode straight away - this is due to the way VSCode refreshes the file preview. If this is the case, just close the file editor tab and open it again.</br>



### Sell <a name="sell"></a>
A function to sell an item. Takes 2 options:</br>
`--product_name` - a name to a product</br>
`--sell_price` - price at which we are selling it</br>
Sold inventory is logged in `sold.csv` file. Columns are:[ProductName,SoldDate,SalePrice,OriginalPrice].</br>
We assume that we can sell something **at least** 1 day after we bought it to the stock. This is of course easily adjustable by changing `<` to `<=` on line `32` in file `buy_sell_functions.py` if you want to be able to sell on the same day. I kept it like this, so we can play with date functions a bit more :).</br>
So let's assume we want to sell a parrot we bought earlier. First let's move the date a bit further:</br>
`python3 main.py date advance_date --days 1` </br>
Which returns:</br>
`It is now 2023-12-20, hope you are happy.`</br>
Now we can sell it! Use selling command like this:</br>
`python3 main.py sell --product_name parrot --sell_price 8` </br>
Which should give you a result like: </br>
`One parrot sold!`</br>
Now if we try to sell a parrot again (which we don't have anymore):</br>
`python3 main.py sell --product_name parrot --sell_price 8` </br>
We should get a result like: </br>
`Out of stock, buddy`</br>
The sale only goes through if:</br>
a. "Today" is smaller than the expiration date</br>
b. "Today" is bigger than than the date an item was added to the stock</br>
c. The sale price is higher than the price we bought it for</br>


## Reporting <a name="reporting"></a> 

All reporting related code can be found in `reporting_functions.py` file.

### List inventory <a name="inventory"></a>
A function to list today's stock. Needs no arguments. To be fair, did not see a point of passing a specific date, if we can just change today's date and check there. Use it as below:</br>
`python3 main.py report inventory`</br>
Which will give you a result like this (on a day of 2023-12-20):</br>
```
[Product_name, Purchase_date, Price, Expiry_date]
['apple', '2023-12-17', '6', '2023-12-22']
['tea', '2023-12-19', '5', '2024-01-02']
['banana', '2023-12-20', '7', '2024-03-05']
```

### Report revenue <a name="revenue"></a>
A function to get a revenue of a given day/month/year. Accept a variety of possible dates, such as in format `YYYY-MM-DD`, `YYYY-MM`, `YYYY`, but also options like `yesterday`, `today`, or even `tomorrow`. Let's see two examples:</br>
Example 1 - running:</br>
`python3 main.py report revenue --date 2023`</br>
Will return just a number:</br>
`83`</br>
Example 2 - running:</br>
`python3 main.py report revenue --date yesterday`</br>
Will return:</br>
`No revenue in that date range!`

### Report profit <a name="profit"></a>
A function to get a profit of a given day/month/year. Accept a variety of possible dates, such as in format `YYYY-MM-DD`, `YYYY-MM`, `YYYY`, but also options like `yesterday`, `today`, or even `tomorrow`. Let's see two examples:</br>
Example 1 - running:</br>
`python3 main.py report profit --date 2023-12`</br>
Will return just a number:</br>
`28`</br>
Example 2 - running:</br>
`python3 main.py report profit --date tomorrow`</br>
Will return:</br>
`No profit in that date range!`


### Reporting files <a name="rep-files"></a>
This is an extra built-in into all reporting functions, such as any call to them will be logged - yes, that includes a call to `list_inventory()` before making a sale. All those requests are stored in 2 files: `reports_log.csv` and `report_log_json.json`. Let's see how they look inside:</br>
`reports_log.csv` is your regular CSV, with columns as [DateOfReport,ActualDateOfReport,TypeOfReport,Result] and will have some data like:</br>
```
DateOfReport,ActualDateOfReport,TypeOfReport,Result
"2024-02-04","2023-12-16","profits","Requested for: 2023 - profit is 24"
"2024-02-04","2023-12-16","profits","Requested for: 2025 - No profits :( )"
"2024-02-04","2023-12-16","revenue","Requested for: 2025 - No revenue :( )"
"2024-02-04","2023-12-16","revenue","Requested for: 2023 - revenue is 75"
"2022-02-04","2023-12-16","inventory","[['apple', '2023-12-17', '6', '2023-12-22'], ['tea', '2023-12-19', '5', '2024-01-02'], ['banana', '2023-12-20', '7', '2024-03-05']]"
"2020-03-04","2023-12-16","inventory","It is empty"
``` 
</br>

`report_log_json.json` is also just a regular JSON dataset, which will store requests like:</br>
```
{
    "DateOfReport": "2023-12-20",
    "ActualDateOfReport": "2023-12-20",
    "TypeOfReport": "inventory",
    "Result": "[['apple', '2023-12-17', '6', '2023-12-22'], ['tea', '2023-12-19', '5', '2024-01-02'], ['banana', '2023-12-20', '7', '2024-03-05']]"
}
{
    "DateOfReport": "2023-12-20",
    "ActualDateOfReport": "2023-12-20",
    "TypeOfReport": "revenue",
    "Result": "Requested for: 2023 - revenue is 83"
}
{
    "DateOfReport": "2023-12-20",
    "ActualDateOfReport": "2023-12-20",
    "TypeOfReport": "revenue",
    "Result": "Requested for: 2023-12-19 - No revenue :( )"
}
```
