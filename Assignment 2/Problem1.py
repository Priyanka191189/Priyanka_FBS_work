# Convert the time entered in hh,min and sec into seconds.
hrs = float(input("Enter no. of hrs: "))
min = float(input("Enter no. of min: "))
sec = float(input("Enter no.of sec: "))

#Convert hr to sec.
hrs_to_sec = hrs*3600
min_to_sec = min*60
sec_same = sec
print("Hours :  ", hrs_to_sec)
print("Minutes: ", min_to_sec)
print("Seconds : ", sec)   
print("Hours:  ", hrs_to_sec, "Minuts :  ", min_to_sec, "Seconds : ", sec)
total = hrs_to_sec + min_to_sec
print("Total seconds:  ", total) 


