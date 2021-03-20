import random
i=0
while(i<=10):

    list=["snake","water","gun"]
    choice=random.choice(list)
    my_choice=input("Enter your choice\n")
    if(choice=="snake" and my_choice=="water"):
        print("You loose")
    elif(choice=="water" and my_choice=="gun"):
        print("You loose")
    elif(choice=="gun" and my_choice=="snake"):
        print("You loose")
    elif(choice=="water" and my_choice=="snake"):
        print("You won")
    elif(choice=="gun" and my_choice=="water"):
        print("You won")
    elif(choice=="snake" and my_choice=="gun"):
        print("You won")
    else:

        print("max attempt reached")
    
    i=i+1
