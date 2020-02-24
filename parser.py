import csv
import asyncio

cdli_atf=open("cdliatf_unblocked.atf", "r")
cdli_data = cdli_atf.readlines()

cdli_catalogue_csv = csv.DictReader(open("cdli_catalogue.csv", "r"))
cdli_catalogue = []
for line in cdli_catalogue_csv:
    cdli_catalogue.append(line)

cdli_catalogue = []
genre_list = []

def list_of_genres():
    cdli_catalogue_csv = open("cdli_catalogue.csv", "r")
    cdli_catalogue_data = csv.DictReader(cdli_catalogue_csv)
    for line in cdli_catalogue_data:
        cdli_catalogue.append(line)

    genre_set = set()
    for item in cdli_catalogue:
        genre_set.add(item["genre"])
    genre_list = list(genre_set)
    cdli_catalogue_csv.close()
    return genre_list

def print_to_file(starting_line, file):
    file.write(cdli_data[starting_line])
    for i in range(starting_line+1, len(cdli_data)):
        line = cdli_data[i]
        if(line.find("&P")==-1):
            file.write(line)
        else:
            break

def translated_sumerian ():
    sumerian_translated = open("sumerian_translated.atf","w")

    for i in range(len(cdli_data)):

        line = cdli_data[i]
        starting_line = i-1
        last_line = i+1

        if(line.find("#atf:") !=-1 and line.find("lang") !=-1 and line.find("sux") !=-1):

            while(starting_line>=0):
                if(cdli_data[starting_line].find("&P")==-1):
                    starting_line-=1
                else:
                    break

            while(last_line < len(cdli_data) and cdli_data[last_line].find("&P")==-1):
                if(cdli_data[last_line].find("#tr.en:")!=-1):
                    print_to_file(starting_line, sumerian_translated)
                    break

                last_line+=1
    sumerian_translated.close()
    print("\nYour requested data has been printed into sumerian_translated.atf\n")

def all_sumerian():
    sumerian_untranslated = open("sumerian_untranslated.atf","w")

    for i in range(len(cdli_data)):

        line = cdli_data[i]
        starting_line = i-1

        if(line.find("#atf:") !=-1 and line.find("lang") !=-1 and line.find("sux") !=-1):

            while(starting_line>=0):
                if(cdli_data[starting_line].find("&P")==-1):
                    starting_line-=1
                else:
                    break

            print_to_file(starting_line, sumerian_untranslated)
    sumerian_untranslated.close()
    print("\nYour requested data has been printed into sumerian_untranslated.atf\n")

def catalogue(genre):
    genre_atf = open("genre.atf", "w")
    for i in range(len(cdli_data)):
        line = cdli_data[i]
        if(line.find("&P") !=-1):
            idlist = line.split()
            id = (idlist[0])[2:]
            for item in cdli_catalogue:
                if item["id_text"] == id:
                    if(item["genre"]==genre):
                        print_to_file(i, genre_atf)
                    else:
                        break
    genre_atf.close()
    print("\nYour requested data has been printed into genre.atf\n")


print("\nHi, welcome to the cdli data extractor script\n")
print("1\tSumerian language texts.\n2\tSumerian language texts with translation.\n3\tSort by genre.\n ")
first_choice = int(input("Please enter the number corresponding to your choice: "))
if(first_choice==3):
    print("\nEnter the genre number below\n")
    genre_list = list_of_genres()
    for i in range(len(genre_list)):
        print("{}\t{}".format(i+1, genre_list[i]))
    second_choice = int(input("Please enter the number corresponding to your choice: "))
    catalogue(genre_list[second_choice-1])
if(first_choice==1):
    all_sumerian()
if(first_choice==2):
    translated_sumerian()

cdli_atf.close()
