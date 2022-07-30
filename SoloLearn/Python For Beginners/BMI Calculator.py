"""Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
It’s calculated using a person's weight and height, using this formula: weight / height²
The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more
Weight is in kg, height is in meters."""
print("What is your name?")
name=input()
print("Weight in kg?")
weight=int(input())
print("Height in m?")
height=float(input())
x=weight/(height**2)
if True:
    if x<18.5:
        y="Underweight"
    elif x<25:
        y="Normal"
    elif x<30:
        y="Overweight"
    else:
        y="Obesity"
print(name +", your BMI is " + y + " (" +str(round(x,1)) + ") with a weight of "+str(weight)+ "kg and a height of "+ str(height)+ "m")
if True:
    if y=="Underweight":
        print("Recommendation: Eat More Pizza")
    elif y=="Normal":
        print("Recommendation: Eat Pizza as Normal")
    elif y=="Overweight":
        print("Recommendation: Eat Less Pizza")
    else:
        print("Recommendation: Consider Breadless Pizza")
