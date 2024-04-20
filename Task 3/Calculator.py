import tkinter as tk

def on_click(button_text):
    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)


root = tk.Tk()
root.title("Calculator")
root.config(bg="black")

fg_color = "white"
bg_color = "black"
button_bg_color = "gray"


entry = tk.Entry(root, width=20, borderwidth=5, bg=bg_color, fg=fg_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


for i, button_text in enumerate(buttons):
    button = tk.Button(root, text=button_text, padx=20, pady=20, bg=button_bg_color, fg=fg_color, 
                       command=lambda b=button_text: on_click(b))
    row = (i // 4) + 1
    col = i % 4
    button.grid(row=row, column=col)


root.mainloop()
