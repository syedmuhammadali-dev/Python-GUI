import tkinter as tk

# Window banayi
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# Input 1
label1 = tk.Label(window, text="Number 1:")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=5, pady=5)

# Input 2
label2 = tk.Label(window, text="Number 2:")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Result box
result_label = tk.Label(window, text="Result:")
result_label.grid(row=2, column=0, padx=5, pady=5)
result_entry = tk.Entry(window)
result_entry.grid(row=2, column=1, padx=5, pady=5)


def show_result(value):
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(value))


def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    show_result(num1 + num2)


def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    show_result(num1 - num2)


def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    show_result(num1 * num2)


def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    show_result(num1 / num2)


def remainder():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    show_result(num1 % num2)


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_entry.delete(0, tk.END)


# Buttons
btn_add = tk.Button(window, text="Add (+)", command=add)
btn_add.grid(row=3, column=0, columnspan=2, pady=3)

btn_sub = tk.Button(window, text="Subtract (-)", command=subtract)
btn_sub.grid(row=4, column=0, columnspan=2, pady=3)

btn_mul = tk.Button(window, text="Multiply (*)", command=multiply)
btn_mul.grid(row=5, column=0, columnspan=2, pady=3)

btn_div = tk.Button(window, text="Divide (/)", command=divide)
btn_div.grid(row=6, column=0, columnspan=2, pady=3)

btn_rem = tk.Button(window, text="Remainder (%)", command=remainder)
btn_rem.grid(row=7, column=0, columnspan=2, pady=3)

btn_clear = tk.Button(window, text="Clear", command=clear)
btn_clear.grid(row=8, column=0, columnspan=2, pady=3)

window.mainloop()
