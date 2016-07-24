# rock-paper-scissors by Dono27
# Bence László
# www.bencelaszlo.cf
import random
oppo = ['rock', 'paper', 'scissors']
round_counter,user_win,oppo_win,draw_score=0,0,0,0
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
        draw_score+=1
    else:
        print('You lose!')
        oppo_win+=1
    round_counter+=1
#results section
user_score=user_win*3+draw_score
oppo_score=oppo_win*3+draw_score
if(user_score>oppo_score):
    print("""
You're the winner!
""")
elif(user_score==oppo_score):
    print("""
    It's a draw.
    """)
elif(oppo_score>user_score):
    print("""
You're loser!
""")
