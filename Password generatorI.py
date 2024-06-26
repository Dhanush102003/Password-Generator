from tkinter import *
from tkinter import messagebox,simpledialog
from random import choice, randint, shuffle

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="light blue")



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
    password_entry.delete(0, END)
    password_entry.insert(0, password)
   
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    wlecome = welcome_label.get()



website_label = Label(text="Website:", bg="light blue", font=("Helvetica", 14, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email ID:", bg="light blue", font=("Helvetica", 14, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="light blue", font=("Helvetica", 14, "bold"))
password_label.grid(row=3, column=0)

website_entry = Entry(width=35, font=("Helvetica", 12))
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.insert(0, "Dhanush Balakrishnan")
website_entry.focus()

email_entry = Entry(width=35, font=("Helvetica", 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=10)
email_entry.insert(0, "dhanush.b1102003@gmail.com")

password_entry = Entry(width=21, font=("Helvetica", 12))
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=15, bg="black", fg="red", font=("Helvetica", 12, "bold"), command=generate_password)
generate_password_button.grid(row=3, column=2)

welcome_label= Label(text="Thanks for coming, have a great day :)......!",bg='pink',pady=10,font=("Helvetiva", 18,"bold"))

welcome_label.grid(row=8,column=1)



window.mainloop()