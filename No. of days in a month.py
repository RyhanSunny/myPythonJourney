months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("List of months: ", months)
month = input("pick a month: ").lower()

list_30_days = ["september", "april", "june", "november"]
list_31_days = ["january", "march", "may", "july", "august", "october", "december"]

if month == "february":
  print(month, " has 28 or 29 days")
elif month in list_30_days:
  print(month, " has 30 days")
elif month in list_31_days:
  print(month, " has 31 days")
else:
  print("Invalid month name")
