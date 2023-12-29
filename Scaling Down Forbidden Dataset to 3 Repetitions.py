import csv

# Opening original dataset file
csvfile_original = open('input_files/forbidden_question_set.csv', encoding='utf-8')
csvreader_original = csv.reader(csvfile_original)
headers = list(next(csvreader_original))

# Opening new, edited dataset file for easier formatting
csvfile_new = open('input_files/forbidden_question_set_new.csv', encoding='utf-8', mode='w', newline='')
csvwriter_new = csv.writer(csvfile_new)
csvwriter_new.writerow(['input_id'] + headers)

# input_id is the unique identifier for each row
input_id = 0
for row in csvreader_original:
    if row[-1] in '012':
        data = list(row)
        csvwriter_new.writerow([input_id] + data)
        print(input_id)
        input_id += 1

# close the file objects
csvfile_original.close()
csvfile_new.close()

