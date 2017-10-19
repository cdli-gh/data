# CDLI Daily Bulk Data Dump
In this folder, you will find the files cdli_catalogue_1of2.csv, cdli_catalogue_2of2.csv, and cdliatf_unblocked.atf

Both are UTF-8 text files, cdli_catalogue has comma separated values and cdliatf files contain plain text. The catalogue file is split in two because of file size limitations at Github. To merge the catalogue files into one, use:
```
cat cdli_catalogue_1of2.csv cdli_catalogue_2of2.csv > cdli_catalogue.csv
```
in the command line, on linux or mac. Under windows, try:
```
copy cdli_catalogue_1of2.csv+cdli_catalogue_2of2.csv cdli_catalogue.csv
```

Before October 18 2017, the catalogue and atf were provided in .zip format.

EPP
cdli@ucla.edu
