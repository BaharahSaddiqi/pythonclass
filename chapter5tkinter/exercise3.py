from tkinter import* 
parent=Tk()
parent.geometry("600x800")
name=Label(parent, text="Name").grid(row=0, column=0)
entry1=Entry(parent).grid(row=0, column=1)
password=Label(parent, text="Password").grid(row=1, column=0)
entry2=Entry(parent).grid(row=1, column=1)
submit=Button(parent, text="Submit").grid(row=3,column=0)







parent.mainloop()