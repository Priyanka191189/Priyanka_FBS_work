#Write a program to convert days into years, weeks and days

days = int(input("Enter no. of days:  "))
years = days//365
days = days % 365   #Reminder
weeks = days//7
days = days % 7
print("No. of years : ", years)
print("No. of Weeks : ", weeks)
print("No. of Days : ", days)
print("No. of years: ", years, "No. of weeks: ", weeks, "No. of days: ", days)