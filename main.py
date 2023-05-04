import tkinter as tk
from sgrEq import sqr_eq


def clicked():
    A = float(arg_A.get())
    B = float(arg_B.get())
    C = float(arg_C.get())
    lbl_result.configure(text=sqr_eq(A, B, C))


def close():
    window.destroy()


window = tk.Tk()
window.title("Square equations super solver 3000")
window.geometry('360x240')
bg = tk.PhotoImage(file='../Users/50000861/AppData/Local/Temp/gradient.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='c')

label_bg = tk.Label(frame, image=bg)
label_bg.place(x=0, y=0)

lbl_A = tk.Label(frame, text='A', font=("Arial", 30), bg='#999900')
lbl_A.grid(column=0, row=0, padx=10, pady=20)
arg_A = tk.Entry(frame, width=15)
arg_A.insert(0, '1')
arg_A.grid(column=0, row=1, padx=10, pady=20)

lbl_B = tk.Label(frame, text='B', font=("Arial", 30))
lbl_B.grid(column=1, row=0, padx=10, pady=20)
arg_B = tk.Entry(frame, width=15)
arg_B.insert(0, '0')
arg_B.grid(column=1, row=1, padx=10, pady=20)

lbl_C = tk.Label(frame, text='C', font=("Arial", 30))
lbl_C.grid(column=2, row=0, padx=10, pady=20)
arg_C = tk.Entry(frame, width=15)
arg_C.insert(0, '0')
arg_C.grid(column=2, row=1, padx=10, pady=20)

lbl_roots = tk.Label(frame, text='ROOTS:')
lbl_roots.grid(column=0, row=2)
lbl_result = tk.Label(frame, text='Enter the values')
lbl_result.grid(column=2, row=2)

btn = tk.Button(frame, text='Calculate', font=("Arial", 15), command=clicked)
btn.grid(column=0, row=3)
exit = tk.Button(frame, text='Cancel', font=("Arial", 15), command=close)
exit.grid(column=2, row=3)

window.mainloop()