import csv


#Initialising variables
number_to_continue_from = 14
TEMPERATURE = 0.0                   # 0.0 0.25 0.5 0.75 1.0

# ONLY CHANGE ABOVE VARIABLES BASED ON WHAT YOU NEED


# Opening original dataset file
csvfile_original = open('input_files/control_dataset_new.csv', encoding='utf-8')
csvreader_original = csv.reader(csvfile_original)
headers = list(next(csvreader_original))
for _ in range(number_to_continue_from):                               
    next(csvreader_original)

# Opening new, edited dataset file for easier formatting
csvfile_new = open('input_files/control_dataset_continued_' + str(TEMPERATURE) + ".csv", encoding='utf-8', mode='w', newline='')
csvwriter_new = csv.writer(csvfile_new)


# input_id is the unique identifier for each row
input_id = number_to_continue_from                                    
for row in csvreader_original:
    data = list(row)
    csvwriter_new.writerow(data)
    print(input_id)
    input_id += 1

# close the file objects
csvfile_original.close()
csvfile_new.close()