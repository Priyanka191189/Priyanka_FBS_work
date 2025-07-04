#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter 3 digit no.: "))   
copy = num 
a = num % 10
num = num//10
b = num % 10
c = num // 10
reverse = a*100 + b *10 + c

if(copy == reverse):
    print("The number is Palidrome")
else:
    print("The no. is not Palidrome")

