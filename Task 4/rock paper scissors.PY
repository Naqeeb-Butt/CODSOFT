import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("500x400")
        self.root.config(bg="lightgray")

        self.choices = ["Rock", "Paper", "Scissors"]

        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.result = tk.StringVar()

        self.player_label = ttk.Label(root, text="Your Choice:", background="lightgray", font=("Arial", 14))
        self.player_label.grid(row=0, column=0, padx=10, pady=10)

        self.rock_button = ttk.Button(root, text="Rock" , image=self.load_image("rock.png"), command=lambda: self.set_player_choice("Rock"))
        self.rock_button.grid(row=0, column=1, padx=10, pady=10)

        self.paper_button = ttk.Button(root, text="Paper", image=self.load_image("paper.png"), command=lambda: self.set_player_choice("Paper"))
        self.paper_button.grid(row=0, column=2, padx=10, pady=10)

        self.scissors_button = ttk.Button(root, text= "Scissors", image=self.load_image("scissors.png"), command=lambda: self.set_player_choice("Scissors"))
        self.scissors_button.grid(row=0, column=3, padx=10, pady=10)

        self.player_image_label = ttk.Label(root, background="lightgray")
        self.player_image_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.computer_label = ttk.Label(root, text="Computer's Choice:", background="lightgray", font=("Arial", 14))
        self.computer_label.grid(row=2, column=0, padx=10, pady=10)

        self.computer_image_label = ttk.Label(root, background="lightgray")
        self.computer_image_label.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

        self.result_label = ttk.Label(root, textvariable=self.result, background="lightgray", font=("Arial", 16))
        self.result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.rock_gif = tk.PhotoImage(file="rock.png")
        self.paper_gif = tk.PhotoImage(file="paper.png")
        self.scissors_gif = tk.PhotoImage(file="scissors.png")

        self.play_button = ttk.Button(root, text="Play", command=self.play, style="Play.TButton")
        self.play_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def set_player_choice(self, choice):
        self.player_choice.set(choice)
        self.show_player_image(choice)

    def play(self):
        player_choice = self.player_choice.get()
        computer_choice = random.choice(self.choices)
        
        self.computer_choice.set(computer_choice)

        if player_choice == computer_choice:
            self.result.set("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            self.result.set("You win!")
        else:
            self.result.set("Computer wins!")

        self.show_images(player_choice, computer_choice)

    def show_images(self, player_choice, computer_choice):
        player_img = self.load_image(player_choice.lower() + ".png")
        computer_img = self.load_image(computer_choice.lower() + ".png")

        self.computer_image_label.configure(image=computer_img)
        self.computer_image_label.image = computer_img

    def show_player_image(self, player_choice):
        player_img = self.load_image(player_choice.lower() + ".png")

        self.player_image_label.configure(image=player_img)
        self.player_image_label.image = player_img

    def load_image(self, filename):
        return tk.PhotoImage(file=filename)

def main():
    root = tk.Tk()
    root.style = ttk.Style()
    root.style.theme_use("clam")  # Use a different theme
    root.style.configure("Play.TButton", background="gray", foreground="white")  # Button style for play button
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
