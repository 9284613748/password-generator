import tkinter as tk
import random
import string

def generate_password(length, include_special_chars=True):
    chars = string.ascii_letters + string.digits
    if include_special_chars:
        char += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        password = generate_password(length)
        result_label.config(text="Your generated password is: " + password)
    except ValueError:
        result_label.config(text="Error: please enter a valid positive integer for password length")

root = tk.Tk()
root.title("Password Generator")


info_label = tk.Label(root, text="welcome to Password Generator!\nEnter the length of the password:")
info_label.pack(pady=10)


length_entry = tk.Entry(root)
length_entry.pack(pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=5)


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
