import random
number=random.randint(1,100)
attempt=0
max_attempt=3
print("Welcome to the random number guessing contest")
print("Guess a random number from 1 to 50: ")
while attempt<max_attempt:
    guess=int(input("Enter the guessed number: "))
    attempt+=1
    if number==guess :
        print("Your guess is correct")
    elif guess>50:
        print("Your guess number should not exit 50")
    else:
        print("Your guess is wrong")
else:
    print("Your attempt to find the answer is over")
