
from tkinter import *
import random

w = Tk()
w.title('Guess A Number Game')
w.geometry('600x400')

# background color for window
w.config(bg='#1B3C53')
w.resizable(width=False, height=False)

# main Logic
ranNum = random.randint(1, 10)
chance = 4
displayResult = StringVar()

def check_guess():
    global ranNum, chance
    userInput = int(user_input.get())

    if chance > 0:
        if userInput == ranNum:
            msg = "You Won! " + str(ranNum) + " is the right number"
            user_input.config(state='disabled')
            guess_button.config(state='disabled')
        elif userInput > ranNum:
            chance = chance - 1
            msg = "Your Guess Is Too High. Think Of A Smaller Number"
            user_input.delete(0, END)
        elif userInput < ranNum:
            chance = chance - 1
            msg = "Your Guess Is Too Low. Think Of A Higher Number"
            user_input.delete(0, END)
    else:
        msg = "Game Over! " + str(chance) + " Attempts Left. The Correct Number Was " + str(ranNum)
        user_input.config(state='disabled')
        guess_button.config(state='disabled')

    displayResult.set(msg)

# Create Widgets
title = Label(w, text='Guess A Number Game', font=('Arial', 20), fg='#FFCC00', bg='#1B3C53')
gameInstruction = Label(w, text='Guess The Number Between 1 to 10 in 4 Attempts',
                        font=('Arial', 13), fg='#FFCC00', bg='#1B3C53')
user_input = Entry(w, font=('Arial', 12))
guess_button = Button(w, text='Guess', font=('Arial', 13), fg='#F5E8C7', bg='#435585', command=check_guess)
exit_button = Button(w, text='Exit', font=('Arial', 14), fg='white', bg='#435585', command=w.destroy)
outputLabel = Label(w, font=('Arial', 14), fg='#FFCC00', bg='#1B3C53', textvariable=displayResult)

# Place Widgets
title.place(x=140, y=50)
gameInstruction.place(x=95, y=95)
user_input.place(x=180, y=150)
guess_button.place(x=370, y=150)
exit_button.place(x=300, y=300)
outputLabel.place(x=100, y=220)

w.mainloop()
