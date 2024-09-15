import csv
import os


# INITIALISE VARIABLES ONLY NEED CHANGE THESE

TEMPERATURES = [0.0, 0.25, 0.5, 0.75, 1.0]
MODELS = ['Llama-2-13B-Chat-GGUF', "Vicuna-33B-V1.3-GGUF", "gpt-3.5-turbo", "Mistral-7B-Instruct-v0.2-GGUF"]
JAILBREAK_OR_NOT = 'jailbreak'            # "jailbreak" "non-jailbreak"
EVALUATION_ERROR = 0.021                  # Constant error made by ChatGPT when evaluating jailbreak or not
TOTAL_RESPONSES = 2880                    # Constant number of responses for jailbreak

# ONLY CHANGE WHAT IS ABOVE

def get_evaluated_responses(content_policy_file):
    evaluated_responses = 0
    with open(content_policy_file, encoding='utf-8') as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)

        for row in csvreader:
            if row[4] == "False":
                evaluated_responses += 1

    return evaluated_responses

def calculate_percentage_error(evaluated_responses, TOTAL_RESPONSES, EVALUATION_ERROR):
    return round(EVALUATION_ERROR * evaluated_responses / TOTAL_RESPONSES, 5)

result = {}

for MODEL in MODELS:
    MODEL_errors = []
    for TEMPERATURE in TEMPERATURES:
        content_policy_file = os.path.join('content_policy_files', MODEL)
        content_policy_file = os.path.join(content_policy_file, JAILBREAK_OR_NOT)
        content_policy_file = os.path.join(content_policy_file, MODEL + ' ' + str(TEMPERATURE) + '.csv')

        evaluated_responses = get_evaluated_responses(content_policy_file)
        percentage_error = calculate_percentage_error(evaluated_responses, TOTAL_RESPONSES, EVALUATION_ERROR)
        # print(MODEL, percentage_error)
        MODEL_errors.append(percentage_error)

    result[MODEL] = MODEL_errors

print(result)








