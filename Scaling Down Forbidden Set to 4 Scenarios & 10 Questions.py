import csv

data = []


# This file can only run if the previous scale down of 5 to 3 repetitions was ran
with open('input_files/forbidden_question_set_new.csv', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    counter = 0
    next(csvreader)
    for row in csvreader:
        if int(row[5]) < 5 and int(row[7]) < 10:
            data.append(row)


# Creates a temporary question set dataset that is smaller scale, with only the first 4 scenarios, taking 10 questions from each scenario
# Remember to replace the old dataset after running this code  
# (Don't forget to rename the temporary file by removing the "temp" at the front)
with open('input_files/temp forbidden_question_set_new.csv', mode='w', newline='', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["input_id","model","temperature","response"])
    index = 0
    for row in data:
        new_row = [index] + row[1:]
        csvwriter.writerow(new_row)
        index += 1
    