import csv

#Initialising variables
number_to_continue_from = 14

# Based on which temperature you are using, or whether the filename requires the temperature at the back
# like "forbidden_question_set_continued_0.0.csv"
# Note that if you run different models and temperatures at the same time they will be referencing from 
# the same input folder with the same filenames
# It is recommended to run one temperature at one time for either jailbreak or non-jailbreak and for any model

filename = 'input_files/forbidden_question_set_continued.csv'


# ONLY CHANGE ABOVE VARIABLES BASED ON WHAT YOU NEED



# Opening original dataset file
csvfile_original = open('input_files/forbidden_question_set_new.csv', encoding='utf-8')
csvreader_original = csv.reader(csvfile_original)
headers = list(next(csvreader_original))
for _ in range(number_to_continue_from):                               
    next(csvreader_original)

# Opening new, edited dataset file for easier formatting
csvfile_new = open(filename, encoding='utf-8', mode='w', newline='')
csvwriter_new = csv.writer(csvfile_new)


# write into new file continued                         
for row in csvreader_original:
    csvwriter_new.writerow(row)

# close the file objects
csvfile_original.close()
csvfile_new.close()