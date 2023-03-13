import openai
import os

# Initialize the OpenAI API key from an environment variable
openai.api_key = os.environ.get('OPENAIKEY')

# Define a function to get a response from OpenAI given a message and a list of previous messages
def get_response(message, messages):
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply, messages

# Define the initial messages to start the conversation
messages = [{"role": "system", "content": "You are a kind helpful assistant."}]

# Start the conversation loop
while True:
    message = input("User: ")
    if message:
        reply, messages = get_response(message, messages)
        print(f"ChatGPT: {reply}")
        with open('data.txt', 'a') as file:
            file.write("Q:" + message + "\n")
            file.write("A:" + reply + "\n\n")
    else:
        break
