import random
num=random.randint(1,10)
num_guesses=0
while(num_guesses<5):
    user=int(input("Welcome to the number game. Enter your guess  (1,10)"))
    num_guesses+=1

    if user<num:
        print("your guess is too low")
    if user>num:
        print("Your guess is too high")
    if user==num:
        break

if num==user:
    print("You guessed the number in",num_guesses,"tries")
else:
    print("You couldnt guess the number.The number is",num)