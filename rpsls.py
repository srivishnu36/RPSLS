import random
import sys

def nametonumber(name):
    if(name=="rock"):
        return 0
    elif(name=="spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        return False
    
def numbertoname(number):
    if(number==0):
        print("Computer chose rock")
    elif(number==1):
        print("Computer chose spock")
    elif(number==2):
        print("Computer chose paper")
    elif(number==3):
        print("Computer chose lizard")
    elif(number==4):
        print("Computer chose scissors")    
   
        
def rpsls(choice):
    print("")
    if(choice=="rock"):
        print("Player chose rock")
        player=nametonumber("rock")
    elif(choice=="spock"):
        print("Player chose spock")
        player=nametonumber("spock")
    elif(choice=="paper"):
        print("Player chose paper")
        player=nametonumber("paper")
    elif(choice=="lizard"):
        print("Player chose lizard")
        player=nametonumber("lizard")
    elif(choice=="scissors"):
        print("Player chose scissors")
        player=nametonumber("scissors")
        
  
    comp=random.randrange(5)
    if(comp==0):
        numbertoname(0)
    elif(comp==1):
        numbertoname(1)
    elif(comp==2):
        numbertoname(2)
    elif(comp==3):
        numbertoname(3)
    elif(comp==4):
        numbertoname(4)    
        
    diff=(comp-player)%5
    if(diff==0):
        print("Player and Computer tie")
    elif(diff==1 or diff==2):
        print("Computer wins")
    elif(diff==3 or diff==4):
        print("Player Wins")
        
        
        
        
while(1):    
    inp=input("Enter your choice. Enter stop to abort")
    rpsls(inp)
    
        
