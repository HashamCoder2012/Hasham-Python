import random
characters="abcdefghijklmnopqrstuvwxyz[]*/-+*&^%%$#@!??/"
password_length=int(input("enter desired password length: "))
password=[]
for i in range(password_length):
    password.append(random.choice(characters))
password=''.join(password)
print("Your new password is: "+ password)
