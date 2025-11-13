"""Program to Create Event-Driven Calculator in Tkinter@AakashNinan IMCA Rollno:02"""
import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row, col = 1, 0
for b in buttons:
    if b == "=":
        btn = tk.Button(root, text=b, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=b, width=5, height=2, command=lambda x=b: press(x))
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_btn = tk.Button(root, text="C", width=22, height=2, command=clear)
clear_btn.grid(row=row, column=0, columnspan=4, pady=5)

root.mainloop()
