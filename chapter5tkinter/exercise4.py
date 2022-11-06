from tkinter import* 
parent=Tk()
parent.geometry("600x800")
name=Label(parent, text="Name").place(x=20,y=60)
entry1=Entry(parent).place(x=80,y=60)
password=Label(parent, text="Password").place(x=20,y=90)
entry2=Entry(parent).place(x=80,y=90)
submit=Button(parent, text="Submit").place(x=20,y=120)







parent.mainloop()