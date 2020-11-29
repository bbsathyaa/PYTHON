#7)Write a program to convert the number of days to ages

days=int(input("enter number of days: "))
years=int(days/365)
remaining_days=int(days%365)
m=int(remaining_days/30)
d=int(remaining_days%30)
print("number of years: ",years," years ",m," months ",d," days")

