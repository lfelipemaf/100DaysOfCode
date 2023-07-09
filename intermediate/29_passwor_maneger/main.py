from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Please make sure that you have not left any field blanked.")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\n"
                                               f"Email: {username}\nPassword: {password}\n Is it OK to save it?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{site} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1, sticky='e')
email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2, sticky='e')
password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3, sticky='e')

# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky='e')
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "lfelpemaf@icloud.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky='e')
password_entry = Entry(width=19)
password_entry.grid(column=1, row=3, sticky='e')

# buttons
gen_password_btn = Button(text="Generate Password", width=12, command=generate_password)
gen_password_btn.grid(column=2, row=3, sticky='e' )
add_btn = Button(text="add", width=33, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky='e')

window.mainloop()