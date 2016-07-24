import random
oppo = ['rock', 'paper', 'scissors']
i,win,x=0,0,0
while(i<3):
    print('Round',i+1)
    user_input = str(input('rock, paper or scissors? '))
    cpu_choise=oppo[random.randint(0,2)]
    if(user_input=='rock' and cpu_choise=='scissors') or (user_input=='paper' and cpu_choise=='rock') or (user_input=='scissors' and cpu_choise=='papír'):
        print('You win!')
        win+=1
    elif(user_input==cpu_choise):
        print('You lose!')
        x+=1
    else:
        print('You lose!')
    i+=1
if(win>1) or (win==1 and x>1):
    print("""
You're the winner!
""")
elif(x==3) or (x==1 and win==1):
    print("""
    It's a draw.
    """)
else:
    print("""
You're loser!
""")
