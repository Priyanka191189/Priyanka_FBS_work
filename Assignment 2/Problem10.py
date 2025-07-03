# Write a program to reverse three-digit number.
num = int(input("Enter three digit no.:  "))   # 128
a = num % 10   #8
num = num // 10  #12
b = num % 10   # 2
c = num // 10  # 1
reverse = a*100 + b*10 + c
sum = a+b+c
print("Reverse three-digit number :", reverse)
print("Sum of three digit no. :  ", sum)