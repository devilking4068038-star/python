# AI chat bot

import datetime
import time
user=(input("enter your username"))
present=datetime.datetime.now().hour
if present>=5 and present<=12:
    print("Good Morning")
elif present>=13 and present<=16:
    print("Good Afternoon")
elif present>=17 and present<=20:
    print("Good Evening")
else:
    print("Good Night")
AI={"hello":"Hi","how are u":"i am an AI chat BOT","do u want to train me":""}
def response():
    choice=str(input("do u want to train me y/n?"))
    if choice=="y":
        ques=input("enter your question ?")
        ans=input("enter your answer u want for yourself:")
        AI[ques] = ans
def response2(Question):
    Question = Question.lower()
    for key in AI:
        if key in Question:
            return AI[key]
    return "I am unable to answer your question, please train me to answer as per your requirement"
while True :
    choice=int(input("enter your choice (1=you want train AI for personal use, 2=you want to use AI,3= to exit)?"))
    if choice==1:
        response()
    elif choice==2:
        Question=input("enter your question ?")
        reply=response2(Question)
        print(reply)
    elif choice==3:
        break
    else:
        continue
