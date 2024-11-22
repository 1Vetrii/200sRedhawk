import math

option = int(input())
string = input()
values = string.split(",")
newvalues = []
if option == 1:
  for i in values:
    newvalues = [int(x)**2 for x in values]
elif option == 2:
  for i in values:
    newvalues = [float(f"{math.sqrt(int(x)):.1f}") for x in values]
elif option == 3:
  prod = int(input())
  for i in values:
    newvalues = [int(x)*prod for x in values]
elif option == 4:
  slope = int(input())
  yint = int(input())
  newvalues = [(int(x)*slope)+yint for x in values]
elif option == 5:
  slope = int(input())
  yint = int(input())
  newvalues = [round((int(x)-yint)/slope) for x in values]
elif option == 6:
  newvalues = [round((math.pi*(int(x)**2)),1) for x in values]
print(newvalues)