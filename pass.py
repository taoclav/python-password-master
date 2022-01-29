from tkinter import *
from subprocess import call
import tkinter
root = Tk()
username = "free_user" #that's the given username
password = "123" #that's the given password

#username entry
username_entry = Entry(root)
username_entry.pack()

#password entry
password_entry = Entry(root, show='*')
password_entry.pack()

def trylogin(): #this method is called when the button is pressed
    #to get what's written inside the entries, I use get()
    #check if both username and password in the entries are same of the given ones
    if username == username_entry.get() and password == password_entry.get():
        print("Correct")
        call(["python", "paint1.py"])
    else:
        print("Wrong")
        print("get the password here: https://pastebin.com/QnJSKyDB")

#when you press this button, trylogin is called
button = Button(root, text="check", command = trylogin) 
button.pack()

#App starter
root.mainloop()