from openai import OpenAI
import csv

client = OpenAI(
    api_key="API KEY HERE"
)

conversation_history = []

run = True

while run:
  user_input = input("You:")

  if user_input.lower() == "quit":
      run = False
      break

  conversation_history.append({"role": "user", "content": user_input})
  print(conversation_history)
    
  response = client.chat.completions.create(
    messages=conversation_history,
    model="gpt-3.5-turbo-0613",
    temperature = 1
  )

  text_reply = response.choices[0].message.content
  print(f"Assistant: {text_reply}")

  conversation_history.append({"role": "assistant", "content": text_reply})

  
with open("conversation_history.csv", 'a', newline='') as f:
    csvwriter = csv.writer(f)
    for entry in conversation_history:
        csvwriter.writerow([entry["role"], entry["content"]])

    # Add two empty lines
    csvwriter.writerow([""])
    csvwriter.writerow([""])

      # Reset conversation_history
conversation_history = []

print("\nConnection closed")