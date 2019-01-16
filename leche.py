import random
number=random.randrange(1,101)

done=False
count=0

while not done:
    count+=1
    #ask a user for a number
    guess=int(input("What is my number?"))

    #see how the number compares to the computer
    if guess>number:
        print('Too high!')

    elif guess<number:
            print("too low!")
    else:
        print("congrats")
        print("it took you",count,"times")
        done=True