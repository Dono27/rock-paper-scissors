# rock-paper-scissors by Dono27
# Bence László
# www.bencelaszlo.cf
from random import *
from tkinter import *

#choice section
def user_choice_rock():
    user_choice = "rock"
    turn(user_choice)
def user_choice_paper():
    user_choice = "paper"
    turn(user_choice)
def user_choice_scissors():
    user_choice = "scissors"
    turn(user_choice)

#gameplay setion
def turn(user_choice):
    oppo = ['rock', 'paper', 'scissors']
    oppo_choice=oppo[randint(0,2)]
    if(user_choice=='rock' and oppo_choice=='scissors') or (user_choice=='paper' and oppo_choice=='rock') or (user_choice=='scissors' and oppo_choice=='paper'):
        turn_result.configure(text="""You win!""")
    elif(user_choice==oppo_choice):
        turn_result.configure(text="""It's a draw.""")
    else:
        turn_result.configure(text="""You're defeated!""")


#main program
main_window = Tk()
main_window.title("Rock-Paper-Scissors - Bence László - www.bencelaszlo.cf")
rock_button = Button(main_window, width=20, text="ROCK!", justify=CENTER, command=user_choice_rock, activebackground='black', activeforeground='white')
paper_button = Button(main_window, width=20, text="PAPER!", justify=CENTER, command=user_choice_paper, activebackground='black', activeforeground='white')
scissors_button = Button(main_window, width=20, text="SCISSORS!", justify=CENTER, command=user_choice_scissors, activebackground='black', activeforeground='white')
turn_result = Label(main_window, width=20, justify=CENTER)
win_text = Label(main_window, width=20, text='WINS', justify=CENTER, bg='black', fg='white')
win_results = Label(main_window, width=20)
draw_text = Label(main_window, width=20, text="DRAWS", justify=CENTER, bg='black', fg='white')
draw_results = Label(main_window, width=20)
defeat_text = Label(main_window, width=20, text="DEFEATS", justify=CENTER, bg='black', fg='white')
defeat_results = Label(main_window, width=20)

#create grid
rock_button.grid(row=2, column=1)
paper_button.grid(row=2, column=2)
scissors_button.grid(row=2, column=3)
turn_result.grid(row=3, column=2)
win_text.grid(row=4, column=1)
win_results.grid(row=5, column=1)
draw_text.grid(row=4, column=2)
draw_results.grid(row=5, column=2)
defeat_text.grid(row=4, column=3)
defeat_results.grid(row=5, column=3)

#mainloop
main_window.mainloop()
