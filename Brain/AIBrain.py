# Api Key
fileopen = open("A.I\\Trial-5\\Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

# Importing

import openai
from dotenv import load_dotenv

# Main Code

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    FileLog = open("Trial-5\DataBase\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nBaby : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nBaby : {answer}"
    FileLog = open("Trial-5\\DataBase\\chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

# reply = ReplyBrain("Hello")
# print(reply)

# while True:
#     kk = input("Enter : ")
#     print(ReplyBrain(kk))