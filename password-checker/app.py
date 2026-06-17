import re
import tkinter as tk
def check_strength():
    password=entry.get()
    score=0
    if len(password)>=8:
       score+=1
    if re.search(r"[A-Z]",password):
       score+=1
    if re.search(r"[a-z]",password):
       score+=1
    if re.search(r"[0-9]",password):
       score+=1
    if re.search(r"[!@#$%^&*()_+=-]",password):
       score+=1
    if score<=2:
       result.config(text="weak password",fg="red")
    elif score==3 or score==4:
       result.config(text="medium password",fg="orange")
    else:
       result.config(text="strong password",fg="green")
root=tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
tk.Label(root, text="Enter Password:", font=("Arial",12)).pack(pady=10)
entry=tk.Entry(root, show="*", width=30)
entry.pack()
tk.Button(root, text="Check Strength",command=check_strength).pack(pady=10)
result=tk.Label(root, text="",font=("Arial",12))
result.pack()
root.mainloop()


