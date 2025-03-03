from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Calling Baby : Please wait for few second. And yes don't forget to Clap to wake me up")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Baby is just picked the call : Wait for few more seconds...")
from Main import MainTaskExecution

def MainExecution():
    Speak("Hello Sir")
    Speak("Welcome back, I'm ready to assist you sir")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "whatsapp message" in Data:
            pass

        elif "turn on the tv" in Data:# Specific COmmand
            Speak("Ok..Turning On The Android TV")

        # elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
        #     Reply = QuestionsAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()
