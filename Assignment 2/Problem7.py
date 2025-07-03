# Find the sum of three-digit number.
num = int(input("Enter three digit no.:  "))  #327   #842
a = num % 10   # 2
b = num // 10  # 84
c = b % 10  # 4
d = b // 10 # 8
sum = a+c+d
print("Sum of three no. :  ", sum)


