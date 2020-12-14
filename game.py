print("\n WELCOME TO NITPICKING WITH STICKPICKING")
print("\n Rules of the game")
print ("\n Pick 1,2,3 or 4 matchsticks at one time out of 21")
print ("\n The one who picks up the last matchstick loses")
a=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
b=5-a
print ("\nComputer picks up %d sticks"% b)
c=21-(a+b)
print ("\nRemaining matchsticks=%d"% c)
d=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
e=5-d
print ("\nComputer picks up %d sticks"% e)
f=c-(d+e)
print ("\nRemaining matchsticks=%d"% f)

g=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
h=5-g
print ("\nComputer picks up %d sticks"% h)
i=f-(g+h)
print ("\nRemaining matchsticks=%d"% i)

j=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
k=5-j
print ("\nComputer picks up %d sticks"% k)
l=i-(k+j)
print ("\nRemaining matchsticks=%d"% l)
print ("\nYou have only one option left that is ONE.")
x=input("\nAM I RIGHT?")
print ("\nLOSER USER")

print ("\nNow let's find out how your luck pans out")
print ("\nLet roll of dice decide the number of matchsticks you pick")
import random

z=input("\nroll the dice")
for x in range(5):
    a=random.randint(1,5)
print ("\nThe dice picked %d sticks"%a)
b=5-a
print ("\nComputer picks up %d sticks"% b)
c=21-(a+b)
print ("\nRemaining matchsticks=%d"% c)

z=input("\nroll the dice")
for x in range(5):
    d=random.randint(1,5)
print ("\nThe dice picked %d sticks"%d)
#d=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
e=5-d
print ("\nComputer picks up %d sticks"% e)
f=c-(d+e)
print ("\nRemaining matchsticks=%d"% f)

z=input("\nroll the dice")
for x in range(5):
    g=random.randint(1,5)
print ("\nThe dice picked %d sticks"%g)
#g=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
h=5-g
print ("\nComputer picks up %d sticks"% h)
i=f-(g+h)
print ("\nRemaining matchsticks=%d"% i)

z=input("\nroll the dice")
for x in range(5):
    j=random.randint(1,5)
print ("\nThe dice picked %d sticks"%j)
#j=int(input('Pick up 1,2,3 or 4 matchsticks \n'))
k=5-j
print ("\nComputer picks up %d sticks"% k)
l=i-(k+j)
print ("\nRemaining matchsticks=%d"% l)
print ("\nYou have only one option left that is ONE.")
x=input("\nAM I RIGHT?")
print ("\nLOSER USER")
print ("\nSEE YOU AROUND")

