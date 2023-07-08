from tkinter import *


def button_clicked():
    km = int(entry.get())
    miles = round(km * 1.60934)
    my_label_result.config(text=miles)


miles = 0

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

my_label = Label(text="Miles", font=("Arial", 12, "normal"))
my_label.grid(column=2, row=0)

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=2)

entry = Entry(width=10)
entry.insert(END, string="miles")
entry.grid(column=1, row=0)


my_label_equal = Label(text="is equal to:", font=("Arial", 12, "normal"))
my_label_equal.grid(column=0, row=1)

my_label_result = Label(text="0", font=("Arial", 12, "normal"))
my_label_result.grid(column=1, row=1)

my_label_km = Label(text="Km", font=("Arial", 12, "normal"))
my_label_km.grid(column=2, row=1)
window.mainloop()
