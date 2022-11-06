from tkinter import*
from turtle import left

top=Tk()
redbutton=Button(top, text="Red" , fg="red")
redbutton.pack(side=RIGHT)
greenbutton=Button(top, text="Green" , fg="green")
greenbutton.pack(side=LEFT)
blackbutton=Button(top, text="Black" , fg="black")
blackbutton.pack(side=TOP)
bluebutton=Button(top, text="Blue" , fg="blue")
bluebutton.pack(side=BOTTOM)

top.mainloop()