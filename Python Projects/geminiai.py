from google.generativeai import GenerativeModel , configure
from tkinter import *

root = Tk()
root.title("Gemini Ai")

configure(api_key="YOUR_APIKEY")

place = 0
flag = 1

model = GenerativeModel("gemini-1.5-pro")

def bot(q,place):
    r = model.generate_content(q)
    lable1 = Label(root,text= "Bot : "+ r.text)
    lable1.grid(row=place+2,column=0)
    place = place + 2

def question():
    global place
    global input
    input = Entry(root,width=50)
    input.grid(row=place,column=1)
    lable = Label(root,text="Enter the question : ")
    lable.grid(row=place,column=0)
    Button(root,text="Send",command=lambda:onclick(place)).grid(row=place+1,column=0)

def wait(i):
    global flag
    flag = i
    

def onclick(plac):
    que = input.get()
    bot(que,plac)
    

question()



root.mainloop()
