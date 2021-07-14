import random
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess=int(input("enter your guess"))
    if guess == number:
        print("you won")
        break
    elif guess<number:
        print("guess was to low, guess a number higher then that")
    else:
        print("guess was to high, guess a number lower then that")
    chances+=1
if not chances<5:
    print("you lose")