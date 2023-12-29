import csv

# Opening questions dataset file
csvfile = open('input_files/questions.csv', encoding='utf-8')
csvreader = csv.reader(csvfile)
headers = list(next(csvreader))

# Creating control dataset file (3 repetitions of each question)
csvfile_open = open('input_files/control_dataset.csv', encoding='utf-8', mode='w', newline='')
csvwriter = csv.writer(csvfile_open)
csvwriter.writerow(['input_id',] + headers + ['response_idx'])

# Writing the new control dataset file (without jailbreak prompts)
input_id = 0
for row in csvreader:
    for response_idx in range(3):
        csvwriter.writerow([input_id,] + list(row) + [response_idx,])
        input_id += 1

# Close file objects
csvfile.close()
csvfile_open.close()