import tkinter as tk
from tkinter import ttk
from checker import strength
from utils import score_password

def run():
    root = tk.Tk()
    root.title("Password Strength Checker")
    root.geometry("350x180")
    root.resizable(False, False)

    tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold")).pack(pady=10)
    
    entry = tk.Entry(root, show="*", width=30, font=("Arial", 10))
    entry.pack(pady=5)
    
    bar = ttk.Progressbar(root, length=200, maximum=5, mode='determinate')
    bar.pack(pady=10)
    
    label = tk.Label(root, text="", font=("Arial", 12), fg="gray")
    label.pack()

    def update(e=None):
        pwd = entry.get()
        bar["value"] = score_password(pwd)
        
        text = strength(pwd)
        colors = {"Very Weak":"red","Weak":"orange","Moderate":"yellow","Strong":"light green","Very Strong":"green"}
        label.config(text=text, fg=colors.get(text, "gray"))

    entry.bind("<KeyRelease>", update)
    root.mainloop()

if __name__ == "__main__":
    run()