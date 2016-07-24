# rock-paper-scissors by Dono27
# Bence László
# www.bencelaszlo.cf
from random import *
from tkinter import *
oppo = ['rock', 'paper', 'scissors']
turn_counter,user_win,oppo_win=0,0,0

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

#gameplay section
def turn(user_choice):
    if(turn_counter<3):
        oppo_choice=oppo[randint(0,2)]
        if(user_choice=='rock' and oppo_choice=='scissors') or (user_choice=='paper' and oppo_choice=='rock') or (user_choice=='scissors' and oppo_choice=='papír'):
            turn_result.configure(text="You win!")
            user_win+=1
        elif(user_choice==oppo_choice):
            turn_result.configure(text="It's a draw.")
        else:
            turn_result.configure(text="You lost!")
            oppo_win+=1
        turn_counter+=1
        title_label2.configure(text=turn_counter)
    else:
        results()
        
#results section
def results():
    if(user_win>oppo_win):
        result.configure(text="You win!")
    elif(oppo_win>user_win):
        result.configure(text="You lost!")

#main program
main_window = Tk()
main_window.title("Rock-Paper-Scissors - Bence László - www.bencelaszlo.cf")
title_label1 = Label(main_window, text="Turn")
title_label2 = Label(main_window, text=turn_counter)
rock_button = Button(main_window, text="ROCK!", command="user_choice_rock")
paper_button = Button(main_window, text="PAPER!", command="user_choice_paper")
scissors_button = Button(main_window, text="SCISSORS!", command="user_choice_scissors")
turn_result = Label(main_window)
result = Label(main_window)

#create grid
title_label1.grid(row=1, column=1)
title_label2.grid(row=1, column=2)
rock_button.grid(row=2, column=1)
paper_button.grid(row=2, column=2)
scissors_button.grid(row=2, column=3)
turn_result.grid(row=3, column=1)
result.grid(row=4, column=1)

#mainloop
main_window.mainloop()
