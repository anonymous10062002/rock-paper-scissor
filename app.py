import random

live=True


userScore=compScore=0

result='Draw'
username=input('Welcome to Rock, Paper & Scissor game. Please enter your name: ')

while live:
    compChoice=str(random.randint(0,4))
    userChoice=input('\n'+'Welcome '+username+'. Please choose below option for your turn:'+'\n'+'''Press 1 for Rock
Press 2 for Paper
Press 3 for Scissor
Press 0 to Quit'''+'\n')

    if userChoice==compChoice:
        True
    elif userChoice=='0':
        live=False
    elif userChoice=='1' and compChoice=='2':
        result='You lost!'
        compScore+=1
    elif userChoice=='1' and compChoice=='3':
        result='You won'
        userScore+=1
    elif userChoice=='2' and compChoice=='1':
        result='You won'
        userScore+=1
    elif userChoice=='3' and compChoice=='1':
        result='You lost!'
        compScore+=1
    elif userChoice=='2' and compChoice=='3':
        result='You lost!'
        compScore+=1
    elif userChoice=='3' and compChoice=='2':
        result='You won'
        userScore+=1
    else:
        False
    print('\n'+result+' '+',your final scores as given below:'+'\n'+username+': '+str(userScore)+'\n'+'Computer: '+str(compScore)+'\n'+'Press 0 to Quit')