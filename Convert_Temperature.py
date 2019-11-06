Temp = input("enter temperature value: ")

try:
  if "." in Temp:
    val = float(Temp)
  else:
    val = int(Temp)
except ValueError:
  print("please enter temp value as numbers (eg 35, 45.4, -5")
  quit()

Unit = input("enter temperature unit: ")

if "C" in Unit.upper():
  degrees = round((9 * val) / 5 + 32, 2)
  new_unit = "Farnheit"
elif "F" in Unit.upper():
  degrees = round((val - 32) * 5 / 9, 2)
  new_unit = "Celcius"
  

print("The temperature is ", degrees, " degree ", new_unit)
