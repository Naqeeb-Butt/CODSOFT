import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x200")
        self.root.config(bg="black")
        
        self.length_label = ttk.Label(root, text="Password Length:", background="black", foreground="white")
        self.length_label.pack(pady=(10, 0))

        self.length_entry = ttk.Entry(root, background="black", foreground="black")
        self.length_entry.pack()

        self.complexity_label = ttk.Label(root, text="Password Complexity:", background="black", foreground="white")
        self.complexity_label.pack(pady=(10, 0))

        self.complexity_combobox = ttk.Combobox(root, values=["Low", "Medium", "High"], background="black", foreground="black")
        self.complexity_combobox.pack()

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password, style="Dark.TButton")
        self.generate_button.pack(pady=(10, 0))

        self.result_label = ttk.Label(root, text="", background="black", foreground="white")
        self.result_label.pack(pady=(10, 0))

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_combobox.get()

        if complexity == "Low":
            chars = string.ascii_letters + string.digits
        elif complexity == "Medium":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

        password = ''.join(random.choice(chars) for _ in range(length))
        self.result_label.config(text="Generated Password: " + password)

def main():
    root = tk.Tk()
    root.style = ttk.Style()
    root.style.theme_use("clam")  # Change to dark theme
    root.style.configure("Dark.TButton", background="gray", foreground="black")  # Button style for dark theme
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
