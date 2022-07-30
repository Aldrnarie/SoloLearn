"""You are making a ticketing system.
The price of a single ticket is £100.
For children under 3 years of age, the ticket is free.
Your program needs to take the ages of 5 passengers as input and output the total price for their tickets."""

print("Please give the ages of the 5 passengers")
total = 0
x=0
while True:
    if(int(input())>3):
        total += 100
    else:
        total +=0
    x+=1
    if(x!=5):
        continue
    if(x==5):
        print("Your total price is £" + str(total))
        break
