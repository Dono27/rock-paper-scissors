# rock-paper-scissors by Dono27
# Bence László
# www.bencelaszlo.cf
from random import *
from tkinter import *

#choice section
def user_choice_rock():
    user_choice = "rock"
    turn(user_choice)
    user_image.configure(image=rock_image)
def user_choice_paper():
    user_choice = "paper"
    turn(user_choice)
    user_image.configure(image=paper_image)
def user_choice_scissors():
    user_choice = "scissors"
    turn(user_choice)
    user_image.configure(image=scissors_image)

#gameplay setion
def turn(user_choice):
    oppo = ['rock', 'paper', 'scissors']
    oppo_choice=oppo[randint(0,2)]
    if(oppo_choice=='rock'):
        oppo_image.configure(image=rock_image)
        if(user_choice=='paper'):
            turn_result.configure(text="You Win!", fg="green")
            compare.configure(text=">")
        elif(user_choice=='scissors'):
            turn_result.configure(text="You are defeated!", fg="red")
            compare.configure(text="<")
        else:
            turn_result.configure(text="It is a draw.", fg="gray")
            compare.configure(text="=")
            
    elif(oppo_choice=='paper'):
        oppo_image.configure(image=paper_image)
        if(user_choice=='scissors'):
            turn_result.configure(text="You Win!", fg="green")
            compare.configure(text=">")
        elif(user_choice=='rock'):
            turn_result.configure(text="You are defeated!", fg="red")
            compare.configure(text="<")
        else:
            turn_result.configure(text="It is a draw.", fg="gray")
            compare.configure(text="=")
            
    elif(oppo_choice=='scissors'):
        oppo_image.configure(image=scissors_image)
        if(user_choice=='rock'):
            turn_result.configure(text="You Win!", fg="green")
            compare.configure(text=">")
        elif(user_choice=='paper'):
            turn_result.configure(text="You are defeated!", fg="red")
            compare.configure(text="<")
        else:
            turn_result.configure(text="It is a draw.", fg="gray")
            compare.configure(text="=")
            
#main program
main_window = Tk()
main_window.title("Rock-Paper-Scissors - Bence László - www.bencelaszlo.cf")
rock_button = Button(main_window, width=20, text="ROCK!", justify=CENTER, command=user_choice_rock, activebackground='black', activeforeground='white')
paper_button = Button(main_window, width=20, text="PAPER!", justify=CENTER, command=user_choice_paper, activebackground='black', activeforeground='white')
scissors_button = Button(main_window, width=20, text="SCISSORS!", justify=CENTER, command=user_choice_scissors, activebackground='black', activeforeground='white')
rock_image = PhotoImage(file="dono27_rps/rock.gif")
paper_image = PhotoImage(file="dono27_rps/paper.gif")
scissors_image = PhotoImage(file="dono27_rps/scissors.gif")
user_image = Label(image=rock_image)
user_image.image = rock_image
compare = Label(main_window, justify=CENTER, font=("Helvetica", 30))
oppo_image = Label(image=paper_image)
oppo_image.image = paper_image
turn_result = Label(main_window, width=20, justify=CENTER, font=("Helvetica", 20))

#create grid
rock_button.grid(row=2, column=1)
paper_button.grid(row=2, column=2)
scissors_button.grid(row=2, column=3)
user_image.grid(row=3, column=1)
compare.grid(row=3, column=2)
oppo_image.grid(row=3, column=3)
turn_result.grid(row=4, column=2)

#mainloop
main_window.mainloop()
