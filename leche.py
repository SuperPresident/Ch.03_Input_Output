import random
number=random.randrange(1,101)

done=False
count=0
record=100000000000
print("this is a guess the computers numer game.")
while not done:


    count+=1

    #ask a user for a number
    guess=input("Type a number or Q to quit\r")
    if guess.lower()=="q":
        done=True


    #see how the number compares to the computer

    elif int(guess)>number:
        print('Too high!')

    elif int(guess)<number:
            print("too low!")
    else:
        print("congrats")
        print("it took you",count,"times")
        if count<record:
            record=count
            print("your current record is",record,"times")
            number=random.randrange(1,101)
        count=0