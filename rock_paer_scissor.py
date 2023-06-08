import random
print("Starting the game....")
print()
print("Choose :")
print("\t 1.Rock")
print("\t 2.Paper")
print("\t 3.Scissor")

kitne=int(input("How many timesyou want to play ??"))


for i in range(kitne):
    choice=int(input("Enter your choice : "))
    if(choice==1):
        comp=random.randint(1,4)
        if(comp==1):
            print("Computer Choice : Rock")
            print("....Game Tie....")
            
        elif(comp==2):
            print("Computer Choice : Paper")
            print("....You Loose....")
            
        elif(comp==3):
            print("Computer Choice : Paper")
            print("....You Won....")
          
    elif(choice==2):
        comp=random.randint(1,4)
        if(comp==1):
            print("Computer Choice : Rock")
            print("....You Won....")
           
        elif(comp==2):
            print("Computer Choice : Paper")
            print("....Game Tie....")
            
        elif(comp==3):
            print("Computer Choice : Paper")
            print("....You Loose....")
           
    elif(choice==3):
        comp=random.randint(1,4)
        if(comp==1):
            print("Computer Choice : Rock")
            print("....You Loose....")
            
        elif(comp==2):
            print("Computer Choice : Paper")
            print("....You Won....")
            
        elif(comp==3):
            print("Computer Choice : Paper")
            print("....Game Tie....")
          