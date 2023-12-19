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



## Buy and Sell <a name="buysell"></a> 

Both buy and sell functions can be found in the `buy_sell_functions.py` file.

### Buy <a name="buy"></a>
A function to buy an item into our stock. It takes 3 options:</br>
`--product_name` - to name a product</br>
`--product_price` - price at which we bought it</br>
`--expiration_date` - a date at which the product will expire</br>
Stock is logged in a `stock.csv` file. Columns are:[ProductName,BoughtDate,BoughtPrice,ExpirationDate]</br>
 #### ***Important note:*** Sometimes after something is bought, changes may not reflect in VSCode straight away - this is due to the way VSCode refreshes the file preview. If this is the case, just close the file editor tab and open it again.</br>
Use it as below:</br>
`python3 main.py buy --product_name parrot --buy_price 5 --expiration_date 2024-01-25` </br>
Which should give you a result like: </br>
`Product added to the stock, nice.`



### Sell <a name="sell"></a>

