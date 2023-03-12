import openai
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
openai.api_key = 'sk-'
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    with open('data.txt', 'a') as file:
        file.write("Q:" + message +"\n")
        file.write("A:" + reply + "\n")
        file.write("\n")
    messages.append({"role": "assistant", "content": reply})