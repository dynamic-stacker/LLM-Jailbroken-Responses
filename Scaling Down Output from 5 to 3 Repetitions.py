import csv

#initialising variables

TEMPERATURE = 0.0                           # 0.0 0.25 0.5 0.75 1.0
MODEL = "gpt-3.5-turbo"                     # "Vicuna-33B-V1.3-GGUF" "Llama-2-13B-Chat-GGUF" "Mistral-7B-Instruct-v0.2-GGUF" "gpt-3.5-turbo"
JAILBREAK_OR_NOT = "jailbreak"              # "jailbreak" "non-jailbreak"


# Container
data = []

output_file_name_to_format = MODEL + " " + str(TEMPERATURE) + ".csv"
folder_directory = "output_files/" + MODEL + "/" + JAILBREAK_OR_NOT + "/"

# Read 3 responses out of the 5 from the output file
with open(folder_directory + output_file_name_to_format, encoding='utf-8') as f:
    csvreader = csv.reader(f)
    counter = 0
    next(csvreader)
    for row in csvreader:
        if counter >= 5:
            counter = 0
        if counter in [0, 1, 2]:
            data.append(row)
        counter += 1


# Write data into a temp file
with open(folder_directory + 'temp ' + output_file_name_to_format, mode='w', newline='', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["input_id","model","temperature","response"])
    index = 0
    for row in data:
        new_row = [index] + row[1:]
        csvwriter.writerow(new_row)
        index += 1
    