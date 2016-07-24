# rock-paper-scissors by Dono27
# Bence László
# www.bencelaszlo.cf
import random
oppo = ['rock', 'paper', 'scissors']
round_counter,user_win,oppo_win=0,0,0
user_name = input("What's your name? ")
#gameplay section
while(round_counter<3):
    print('Round',round_counter+1)
    user_input = str(input('Rock, paper or scissors? '))
    oppo_choise=oppo[random.randint(0,2)]
    if(user_input=='rock' and oppo_choise=='scissors') or (user_input=='paper' and oppo_choise=='rock') or (user_input=='scissors' and oppo_choise=='papír'):
        print('You win!')
        user_win+=1
    elif(user_input==oppo_choise):
        print("""It's a draw!""")
    else:
        print('You lose!')
        oppo_win+=1
    round_counter+=1
    print("""

    """)
#results section
print("""


""")
if(user_win>oppo_win):
    print(user_name," is the winner!")
elif(oppo_win>user_win):
    print(user_name," is a loser!")
