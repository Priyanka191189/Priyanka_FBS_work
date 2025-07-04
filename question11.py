# 11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
a1 = 24
a2 = 11
a3 = 50
a4 = 65
a5 = 25
amt = 100

if(a1 < 12):  
    fair1 = amt -amt*0.3
elif(a1 > 59):
    fair_1 = amt -amt*0.5
else:
    fair_1 = amt
print("Cost of a1 = ", fair_1)

if(a2 < 12):  
    fair_2 = amt -amt*0.3
elif(a2 > 59):
    fair_2 = amt -amt*0.5
else:
    fair_2 = amt
print("Cost of a2 = ", fair_2)

if(a3 < 12):  
    fair_3 = (amt -(amt*0.3))
elif(a3 > 59):
    fair_3 = amt -(amt*0.5)
else:
    fair_3 = amt
print("Cost of a3 = ", fair_3)

if(a4 < 12):  
    fair_4 = (amt -(amt*0.3))
elif(a4 > 59):
    fair_4 = amt -(amt*0.5)
else:
    fair_4 = amt
print("Cost of a4 = ", fair_4)

if(a5 < 12):  
    fair_5 = (amt -(amt*0.3))
elif(a5 > 59):
    fair_5 = amt -(amt*0.5)
else:
    fair_5 = amt
print("Cost of a5 = ", fair_5)

total_fair = fair_1 + fair_2 + fair_3 + fair_4 +fair_3
print(total_fair)