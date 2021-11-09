# CDLI Daily Bulk Data Dump
The repository contains a daily dump of all public catalogue and text data from the Cuneiform Digital Library Initiative.

## Format
### Text Data
The CDLI transliterations dump is offered in plain text UTF-8 ATF format.
For more information about ATF, visit : http://oracc.museum.upenn.edu/doc/help/editinginatf/cdliatf/index.html (Scroll down for an example).


### Catalogue data
The catalogue is offered in a UTF-8 comma separated format. Most fields are thoroughly explained here: https://cdli.ucla.edu/?q=cdli-search-information  
Our data schema is currently being remodeled, get in touch if you would like a sneak peak!

To view a sample of the catalogue, you can use the head command on a Unix machine using this syntax, while you are in the directory where the file is stored:
```
head cdli_catalogue_1of2.csv
```
With Windows Power Shell, try
```
Get-Content *filename* -Head *n*
```

EPP cdli@ucla.edu
