import random

def play():
    user = input("Select 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['rock','paper','scissors'])
    
    if user == computer[0]:
        print("Computer has "+computer)
        return 'its a tie :)'
    
    if winner(user,computer):
        print("Computer has "+computer)
        return 'You won :)'
    
    print("Computer has "+computer)
    return 'You Lost :('

def winner(player,opponent):
    if (player == 'r' and opponent[0] == 's') or (player == 's' and opponent[0]=='p') or (player =='p'and opponent[0]=='r'):
        return True

print(play())