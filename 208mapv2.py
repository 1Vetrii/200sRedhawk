import math

option = int(input())
numbers = input().split(",")
if option == 1:
  map = map(lambda x: int(x)**2,numbers)

if option == 2:
  map = map(lambda x: round(math.sqrt(int(x)),1),numbers)

if option == 3:
  integer = int(input())
  map = map(lambda x: int(x)*integer,numbers)

if option == 4:
  slope = int(input())
  yint = int(input())
  map = map(lambda x: (int(x)*slope)+yint,numbers)

if option == 5:
  slope = int(input())
  yint = int(input())
  map = map(lambda x: round((int(x)-yint)/slope),numbers)
  
if option == 6:
  map = map(lambda x: round((math.pi*(int(x)**2)),1),numbers)
  
print(list(map))
