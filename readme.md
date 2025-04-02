# Concert Analysis

Python scripts to analyze your personal concert history.

## How to run

For a description on how to run the script, run the following in a terminal:
```
python .\concert_analysis.py -h
```
The usage is described as followed:

```
usage: concert_analysis.py [-h] --csv CSV [--test] [--plot]

Analyze concerts data given a CSV file. The CSV file must use ',' as separator and must contain 4 columns: 'Date' (in DD/MM/YYYY format), 'Bands' (if      
multiple bands, they must be separated by ';'), 'City' and 'Venue'.

optional arguments:
-h, --help  show this help message and exit
--csv CSV   Path to the CSV file containing the concerts data.
--test      Run some test cases.
--plot      Generate plots of the number of concerts and bands seen by month and by year.
```