from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [random.choice(letters) for _ in range(random.randint(8, 18))]
    pwd_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pwd_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_chars = pwd_letters + pwd_symbols + pwd_numbers
    random.shuffle(password_chars)

    password_text = "".join(password_chars)
    password_entry.delete(0, END)
    password_entry.insert(END, password_text)
    pyperclip.copy(password_text)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website_name = website_entry.get()
    email_user_name = email_uname_entry.get()
    password_text = password_entry.get()

    if len(website_name) == 0 or len(email_user_name) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any fields blank!")
    else:
        ok_to_save = messagebox.askokcancel(title=website_name,
                                            message=f"These are the details entered: \n"
                                                    f"Email: {email_user_name} \n"
                                                    f"Password: {password_text} \n"
                                                    f"Is it OK to save? ")

        if ok_to_save:
            pwd_dict = {
                website_name: {
                    "email": email_user_name,
                    "password": password_text
                }
            }
            passwords_dict = {}
            # Read password.json file in try-catch style - just in case password.json doesn';'t exist.
            try:
                pwd_file = open(file="password.json", mode="r")
            except FileNotFoundError:
                pwd_file = open(file="password.json", mode="w")
                json.dump(pwd_dict, pwd_file, indent=4)
            else:
                passwords_dict = json.load(pwd_file)
                passwords_dict.update(pwd_dict)
                pwd_file = open(file="password.json", mode="w")
                json.dump(passwords_dict, pwd_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                pwd_file.close()



# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        pwd_file = open(file="password.json", mode="r")
    except FileNotFoundError:
        messagebox.showerror(title="Uh-oh!!", message="No Data in the Passwords Bank")
    else:
        passwords_dict = json.load(pwd_file)
        website_name = website_entry.get()
        try:
            pwd_dict = passwords_dict[website_name]
        except KeyError:
            messagebox.showerror(title="Not Found", message=f"No Details found for {website_name}")
        else:
            messagebox.showinfo(title=f"{website_name}", message=f"Detail for {website_name} as follows:\n"
                                                                 f"Email:{passwords_dict[website_name]['email']}\n"
                                                                 f"Password:{passwords_dict[website_name]['password']}\n")
        pwd_file.close()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
# canvas.pack()
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
email_uname_label = Label(text="Email/UserName:")
password_label = Label(text="Password:")

website_entry = Entry(width=30)
email_uname_entry = Entry(width=50)
password_entry = Entry(width=30)
generate_password()

website_entry.focus()
email_uname_entry.insert(END, "vibinvarghese@mydomain.com")

search_button = Button(text="Search", width=20, command=search_website)
gen_password_button = Button(text="Generate Password", width=20, command=generate_password)
add_button = Button(text="Add", width=36, command=add_password)

website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)

email_uname_label.grid(row=2, column=0)
email_uname_entry.grid(row=2, column=1, columnspan=2)

password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
gen_password_button.grid(row=3, column=2)

add_button.grid(row=4, column=1)

window.mainloop()
