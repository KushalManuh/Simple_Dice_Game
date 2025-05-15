import random
dice=0
sp1=0
sp2=0
print("Play player 1")
while True:
    choice=input("Would you like to Roll (r) or Stop (s)?: ").lower()
    if choice=="r":
        dice=random.randint(1,6)
        if dice==1:
            print("Dice rolled 1...")
            print("Player 1 score=0")
            sp1=0
            print()
            break
        else:
            print("Dice rolled", dice)
            sp1+=dice
            print("Player 1 score=", sp1)
    elif choice=="s":
        print("Player 1 score =",sp1)
        print()
        break
    else:
        print("Invalid Choice")
        
print("Play player 2")
while True:
    choice=input("Would you like to Roll(r) or Stop(s)?: ").lower()
    if choice=="r":
        dice=random.randint(1,6)
        if dice==1:
            print("Dice rolled 1...")
            print("Player 2 score=0")
            sp2=0
            print()
            break
        else:
            print("Dice rolled", dice)
            sp2+=dice
            print("Player 2 score=", sp2)
    elif choice=="s":
        print("Player 2 score =",sp2)
        print()
        break
    else:
        print("Invalid Choice")
print("---------------------------------------------------------------------------")
print("Results: ")
print()
print("Player 1 scored", sp1)
print("Player 2 scored", sp2)
if sp1>sp2:
    print("Player 1 wins!")
elif sp1<sp2:
    print("Player 2 wins!")
else:
    print("It's a draw!")
