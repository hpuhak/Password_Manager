from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# --- FIND PASSWORD --- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# --- PASSWORD GENERATOR --- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    #password = ""
    #for char in password_list:
    #  password += char

# --- SAVE PASSWORD --- #
def save_data():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Whoopsie", message="Please make sure you haven't left any fields empty.")
    else:
        #is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: {email_entry.get()} \nPassword: {password_entry.get()} \nIs it ok to save?")
        #if is_ok:
        try:
            with open("data.json", "r") as file:
                #file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                # Read the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        # if try block is successful:
        else:
            # Update the old data with new data:
            data.update(new_data)
            with open("data.json", "w") as file:
                # Save the updated data:
                json.dump(new_data, file, indent=4)
        # whether try block is success or not:
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# --- UI SETUP --- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Stretch columns and fill up the space
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo3.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

# Search
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="ew")

# Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e")
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "my.email@here.com")

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="ew")
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="ew")

# Add Button
add_button = Button(text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()