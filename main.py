#Odd and even battle

import random

computer=random.choice(range(1,11))

yourwish=input("Enter your wish:")
you=int(input("Enter your number:"))


print("Your choice is",you)
print("Computer choice is",computer)

print("And your sum is:",you+computer)

if(yourwish=="Even" and (you + computer)%2==0):
    print("YOU WON")
elif(yourwish=="Even" and (you + computer)%2!=0):
    print("YOU LOSE")
elif(yourwish=="Odd" and (you + computer)%2==0):
    print("YOU LOSE")
elif(yourwish=="Odd" and (you + computer)%2!=0):
    print("YOU WON")
else:
    print("incorrect input")