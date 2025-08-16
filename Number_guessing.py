import random
def game():
    ch=7
    while(True):
        print("Hi welcom to number guessing.\n You have 7 chances to guess a number.\enter low limit and high limit.")
        low=int(input("Enter low number: "))
        high=int(input("Enter High Number: "))
        if(high-low<ch):
            print("The difference should be greater than 7.")
            continue
        else:break
    num=0
    choice=random.randint(low,high)
    while(num<ch):
        num+=1
        n=int(input("Enter a number"))
        if(n>choice):
            print("Too High")
        elif(n<choice):
            print("Too low")
        else:
            print("You won")
            return 0
        print("Tries Left: ",ch-num)
    print("Sorry your 7 tries are over.")
    return 0
game()



