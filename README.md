# Welcome to SuperPy! 

Below you will find the explanation of this little command-line tool powered by argparse, csv, datetime, and several liters of tea.

## Three Notable functions
1. **Reporting system** - you can ask report on profit/revenue for some given date/daterange such as _YYYY-MM-DD, YYYY-MM, YYYY, yesterday, today, tomorrow_. You can also ask for inventory report - that will always show for today.
Commands supported such as:</br>
`python3 main.py report inventory`</br>
`python3 main.py report profit --date today`</br>
`python3 main.py report profit --date yesterday`</br>
`python3 main.py report profit --date tomorrow`</br>
`python3 main.py report profit --date 2023-12-18`</br>
`python3 main.py report profit --date 2023-12`</br>
`python3 main.py report profit --date 2023`</br>
`python3 main.py report revenue --date today`</br>
`python3 main.py report revenue --date yesterday`</br>
`python3 main.py report revenue --date tomorrow`</br>
`python3 main.py report revenue --date 2023-12-18`</br>
`python3 main.py report revenue --date 2023-12`</br>
`python3 main.py report revenue --date 2023`</br>

This was quite a play with dates and ranges and took a lot of time testing. The reason `inventory` is implemented only for `today` is because I felt it makes more sense like that - to get the actual stock for today, *especially since we can modify what "today" is*.


2. **Date system** - current date is stored in the file called `date`. That date can be modified using advance date option to move it further or reset it to actual today's date. Date is stored in YYYY-MM-DD format.

Commands supported such as:</br>
`python3 main.py date today`</br>
`python3 main.py date reset_date`</br>
`python3 main.py date advance_date --days 2`</br>

This was suprisingly easier implement than I expected. While it was not asked to implement `reset` option, it really felt like it had to be there - `advance_date` may take us too far into the future.


3. **Reports storing system** - every report ever requested is stored in a *report_log.csv* file, as well as *report_log_json.json* file, in .csv and .json formats.
Fileds are:
`DateOfReport,ActualDateOfReport,TypeOfReport,Result`

Implementing this was not difficult, but rather tedious, as it took some testing to find what looks better.

***Exporting to JSON, along with using Rich for output, are the extra 2 function picked.***

**MISC**</br>
Some example values were filled for inventory and sold items using GPT3.5 - just to generate a whole bunch of examples faster.
You can add yours using `buy` and `sell` commands as intended of course :)
