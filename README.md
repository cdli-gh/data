# CDLI Daily Bulk Data Dump

**Last update was August 2022. Head to the [open-data] (https://github.com/cdli-gh/open-data) repository for the current data dumps**   
  
The repository contains a daily dump of all public catalogue and text data from the Cuneiform Digital Library Initiative. 

## Getting the data

Make sure you have the Git Large File Storage extensions ([`git-lfs`](https://github.com/git-lfs/git-lfs)) installed, see [here](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) for instructions. For installing under, say, Ubuntu, you can also use.

    $> curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    $> sudo apt-get install git-lfs
  
Clone the repository.

    $> git clone https://github.com/cdli-gh/data --depth 1
  
Retrieve Git LFS data:
  
    $> cd data
    $> git lfs fetch

## Format
### Text Data
The CDLI transliterations dump is offered in plain text UTF-8 ATF format.
For more information about ATF, visit:

      http://oracc.museum.upenn.edu/doc/help/editinginatf/cdliatf/index.html (Scroll down for an example).


### Catalogue data
The catalogue is offered in a UTF-8 comma separated format. Most fields are thoroughly explained here:

     https://cdli.ucla.edu/?q=cdli-search-information  
Our data schema is currently being remodelled, get in touch if you would like a sneak peek!

View a sample of the catalogue, you can use the head command on a Unix machine using this syntax, while you are in the directory where the file is stored:
```
head cdli_catalogue_1of2.csv
```
With Windows Power Shell, try.
```
Get-Content *filename* -Head *n*
```

EPP cdli@ucla.edu
