#Write a program to enter P, T, R and calculate Compound Interest.

P = int(input("Enter Principle amount: "))
T = int(input("Enter no. of years: "))
R = float(input("Enter rate of interest: "))
CompoundInterest = (P*(1+R)**T)
print("Compound Interest : ", CompoundInterest)