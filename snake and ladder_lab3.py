import random #import the random function to generate random no. for the game
count=0 # position of the dice starts from initial value zero
r=0 #initialise the random no. value as zero 
while count<=100: #check the condition
    roll=input("Press r to roll a dice") 
    if roll=='r': #compare roll with r
       r=random.randint(1,6) #generates the value from 1 to 6
    count=count+r #increment count value by r variable
    print("Your random number is",r)
    print("Your count", count)
    print(input("Press any key to exit"))
    if count==38:
            count=9
            print("You have bitten by snake")
            print("Your count is",count)
    elif count==11:
            count=2
            print("You have bitten by snake")
            print("Your count is",count)
    elif count==25:
            count=4
            print("You have bitten by snake")
            print("Your count is",count)
    elif count==40:
            count=68
            print("You have to climb the ladder")
            print("Your count is",count)
    elif count==52:
            count=81
            print("You have to climb the ladder")
            print("Your count is",count)
    elif count==65:
            count=46
            print("You have bitten by snake")
            print("Your count is",count)
    elif count==76:
            count=97
            print("You have to climb the ladder")
            print("Your count is",count)
    elif count==93:
            count=64
            print("You have bitten by snake")
            print("Your count is",count)
    elif count==13:
            count=34
            print("You have to climb the ladder")
            print("Your count is",count)
    elif count==8:
            count=37
            print("You have to climb the ladder")
            print("Your count is",count)
    elif count==89:
            count=70
            print("You have bitten by snake")
            print("Your count is",count)
            
             
