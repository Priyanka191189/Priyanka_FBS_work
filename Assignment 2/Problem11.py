# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
# Rupees 5850 given by minimum notes
amount = int(input("Enter amount given: "))
n500 = amount // 500         #11
r_amount = amount % 500       #350
n200 = r_amount // 200        # 1
r_amount = r_amount % 200       #150
n100 = r_amount // 100        #1
r_amount = r_amount % 100       #50
n50 = r_amount // 50
r_amount = r_amount % 50

print("Notes for 500:  ", n500)
print("Notes for 200:  ", n200)
print("Notes for 100:  ", n100)
print("Notes for 50:  ", n50)
sum = n500+n200+n100+n50
print("Sum: ", sum)