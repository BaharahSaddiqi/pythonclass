
import tkinter as tk

root= tk.Tk()
root.geometry("500x500")
root.title("this is my first GUI")
label=tk.Label(root, text="hallo world", font=('Arial', 18))
label.pack(padx=20, pady=20)
textbox=tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

button=tk.Button(root, text="Click me ", font=('Arial',10))
button.pack()

root.mainloop()