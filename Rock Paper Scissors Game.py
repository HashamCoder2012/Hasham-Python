import random
def get_user_choice():
    user_choice = input("Enter your choice(rock,paper or sissors): ").lower()
    while user_choice not in ['rock','paper','scissors']:
        print("Invalid choice.Please enter rock,paper or scissors.")
        user_choice=input("Enter your choice(rock,paper,scissors): ").lower()
    return user_choice
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def play_game():
    print("Welcome to Rock Paper Scissors")
    computer_choice=get_computer_choice()
    user_choice= get_user_choice()
    print(f"You chose",user_choice)
    print(f"Computer chose {computer_choice}. ")
    result=determine_winner(user_choice,computer_choice)
    print(result)

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return"Its a tie!"
    elif(user_choice=='rock' and computer_choice=='scissors') or \
    (user_choice=='Paper' and computer_choice=='rock') or\
    (user_choice=='scissors' and computer_choice=='paper'):
        return "You win!"
    else:
        return"Computer win!"
    
if __name__=="__main__":
    play_game()