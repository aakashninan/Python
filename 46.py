"""Program to Display Input Text in Tkinter GUI@AakashNinan IMCA Rollno:02"""
import tkinter as tk

def show_text():
    lbl.config(text=entry.get())

root = tk.Tk()
root.title("Text Display")
root.geometry("300x150")

entry = tk.Entry(root)
entry.pack(pady=10)

btn = tk.Button(root, text="Show Text", command=show_text)
btn.pack(pady=5)

lbl = tk.Label(root, text="")
lbl.pack(pady=10)

root.mainloop()
