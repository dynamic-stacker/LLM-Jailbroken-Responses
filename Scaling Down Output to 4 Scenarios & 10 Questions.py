import csv

# initialising output filename variable
# The initial output file should be of 3 repetitions, can be either jailbreak or non-jailbreak
# This program will reduce the output to fit the first 4 scenarios with each scenario containing 10 questions

TEMPERATURE = 0.0                         # 0.0 0.25 0.5 0.75 1.0
MODEL = "gpt-3.5-turbo"            # "Vicuna-33B-V1.3-GGUF" "Llama-2-13B-Chat-GGUF" "Mistral-7B-Instruct-v0.2-GGUF" "gpt-3.5-turbo"
jailbreak_or_not = "jailbreak"             # "jailbreak" "non-jailbreak"

output_file_name_to_format = MODEL + " " + str(TEMPERATURE) + ".csv"
folder_directory = "output_files/" + MODEL + "/" + jailbreak_or_not + "/"

# ONLY CHANGE ABOVE WHERE NECCESSARY


if jailbreak_or_not == "non-jailbreak":
    jailbreak_or_not_question_counter = 3
    jailbreak_or_not_scenario_counter = 90

else:
    jailbreak_or_not_question_counter = 9
    jailbreak_or_not_scenario_counter = 270

# Initialising a list to store data from csv file
data = []

# Reading the initial output file
with open(folder_directory + output_file_name_to_format, encoding='utf-8') as f:
    csvreader = csv.reader(f)
    question_counter = 0
    next(csvreader)
    for row in csvreader:
        data.append(row)

# Writing previous output to temp output file while including the question id at the back
with open(folder_directory + 'temp ' + output_file_name_to_format, encoding='utf-8', mode='w', newline='') as f:
    csvwriter = csv.writer(f)
    question_counter = 0
    question_id = 0
    for row in data:
        if question_id >= 30:
            question_id = 0

        csvwriter.writerow(row + [question_id])

        question_counter += 1

        if question_counter == jailbreak_or_not_question_counter:
            question_id += 1
            question_counter = 0


# Reset data list
data = []

# Read data from temp output file  
with open(folder_directory + 'temp ' + output_file_name_to_format, encoding='utf-8') as f:
    csvreader = csv.reader(f)
    question_counter = 0
    for row in csvreader:
        data.append([int(row[0])] + row[1:])

# Write temp output to temp2 output file including scenario id at the back
with open(folder_directory + 'temp2 ' + output_file_name_to_format, encoding='utf-8', mode='w', newline='') as f:
    csvwriter = csv.writer(f)
    scenarios = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    scenario_index = 0
    scenario_counter = 0
    for row in data:
        if scenario_index >= 13:
            scenario_index = 0

        csvwriter.writerow(row + [scenarios[scenario_index]])

        scenario_counter += 1

        if scenario_counter == jailbreak_or_not_scenario_counter:
            scenario_index += 1
            scenario_counter = 0


# Reset data list
data = []

# Read temp2 output, only taking the first 10 questions of the first 4 scenarios
with open(folder_directory + 'temp2 ' + output_file_name_to_format, mode='r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        if int(row[-2]) < 10 and int(row[-1]) < 5:
            data.append(row)

# Write temp2's output into temp3 output file
with open(folder_directory + 'temp3 ' + output_file_name_to_format, mode='w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    for row in data:
        csvwriter.writerow(row)

# Reset data list
data = []

# Read temp3 output
with open(folder_directory + 'temp3 ' + output_file_name_to_format, mode='r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)


# Write temp3 output file into temp4 output file including the headers and refreshing the intput id at the front
with open(folder_directory + 'temp4 ' + output_file_name_to_format, mode='w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['input_id', 'model', 'temperature', 'response', 'q_id', 'content_policy_id'])
    index = 0
    for row in data:
        csvwriter.writerow([index] + row[1:])
        index += 1

# Reset data list
data = []

# Read temp4 output file for the input id, model, temperature and response
with open(folder_directory + 'temp4 ' + output_file_name_to_format, mode='r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row[:4])


# Write temp4's sorted data into the final output file
# Remember to rename this file and run the continuation to collect the left over data by removing the "final"
# to replace the old output file
with open(folder_directory + 'final ' + output_file_name_to_format, mode='w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    for row in data:
        csvwriter.writerow(row)