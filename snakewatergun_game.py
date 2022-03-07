#PavanVsComputer
import random
my_score,comp_score=0,0
c=5


#function_definations
def comp_snake(a):
    if a=='gun':
        print("You have won and computer has lost.")
        print("Your guess is %s and computer guess is snake."%a,end=' ')
        return 1
    else:
        print("You have lost and computer has won.")
        print("Your guess is %s and computer guess is snake."%a,end=' ')
        return 0    
def comp_water(a):
    if a=='snake':
        print("You have won and computer has lost.")
        print("Your guess is %s and computer guess is water."%a,end=' ')
        return 1
    else:
        print("You have lost and computer has won.")
        print("Your guess is %s and computer guess is water."%a,end=' ')
        return 0    
def comp_gun(a):
    if a=='water':
        print("You have won and computer has lost.")
        print("Your guess is %s and computer guess is gun."%a,end=' ')
        return 1
    else:
        print("You have lost and computer has won.")
        print("Your guess is %s and computer guess is gun"%a,end=' ')
        return 0
def comp_same():
    pass        




i=1
games=int(input("Enter the no of games you want to play against the computer: "))       
while i<=games:
    x=-1
    b=c-i
    var=['snake','gun','water']
    comp=random.choice(var)
    my=input("Enter your guess : 1.snake 2.water 3.gun : ")
    if my==comp:
        comp_same()
    else:
        if comp=='snake':
            x=comp_snake(my)
        elif comp=='water':
            x=comp_water(my)
        elif comp=='gun':
            x=comp_gun(my)
    if x==1:
        my_score+=1
        print("Your score is %s and computer score is %s"%(my_score,comp_score)) 
        print("You have %s chances left"%b)
    elif x==0:
        comp_score+=1
        print("Your score is %s and computer score is %s"%(my_score,comp_score))
        print("You have %s chances left"%b)
    else:
        print("Both computer and your guess is same so no one gets the point.",end='')
        print("You have %s chances left"%b)   
        print("Your score is %s and computer score is %s"%(my_score,comp_score))  
    i+=1    
if my_score>comp_score:
    print("Pavan wins the game against computer with a score %s"%my_score)
elif comp_score>my_score:
    print("Computer wins the game against pavan with a score %s"%comp_score)
else:
    print("The snake_water_game is tied with an equal score of %s"%my_score) 
                         






    

