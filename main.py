from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(4, 7)
nr_symbols = random.randint(1, 3)
nr_numbers = random.randint(1, 3)

letters_list = [random.choice(letters) for char in range(nr_letters)]
symbols_list = [random.choice(symbols) for sym in range(nr_symbols)]
numbers_list = [random.choice(numbers) for num in range(nr_numbers)]

password_list = letters_list + symbols_list + numbers_list

random.shuffle(password_list)

password = "".join(password_list)


def generate_password():
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    mail = email_entry.get()
    passw = password_entry.get()

    new_data = {
        web: {
            "email": mail,
            "password": passw
        }
    }

    if len(web) < 1 or len(mail) < 0 or len(passw) < 0:
        messagebox.showinfo(title="Missing details", message="Please fill all the fields")
    else:

        try:
            with open("data.json", "r") as data_file:
                # Reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, 'end')

        # is_ok = messagebox.askokcancel(title="Confirm details", message=f"Email: {mail}\nPassword: {passw}")
        # if is_ok:
        #     with open("data.txt", "a") as file:
        #         file.write(f"{web}  |  {mail}  |  {passw}\n")


def find_password():
    web = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", message="No data file found")
        print("No data file found")
    else:
        if web in data:
            credentials = data[web]
            passw = credentials["password"]
            messagebox.showinfo("Credentials", message=f"Website: {web}\nPassword: {passw}")
        else:
            messagebox.showinfo("Not Found", f"No details for {web} found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "jessekimani21@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search = Button(text="Search", command=find_password)
search.grid(row=1, column=2, columnspan=2)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
