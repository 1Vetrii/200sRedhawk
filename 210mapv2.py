import math

def one(x):
  return int(x)**2
  
def two(x):
  return round(math.sqrt(int(x)),1)
  
def three(x):
  return int(x)*integer
  
def four(x):
  return (int(x)*slope)+yint
  
def five(m):
  return round((int(m)-yint)/slope)
  
def six(x):
  return round((math.pi*int(x)**2),1)
  
option = int(input())
numbers = input().split(",")

if option == 1:
  map = map(one,numbers)
  
if option == 2:
  map = map(two,numbers)
  
if option == 3:
  integer = int(input())
  map = map(three,numbers)
  
if option == 4:
  slope = int(input())
  yint = int(input())
  map = map(four,numbers)
  
if option == 5:
  slope = int(input())
  yint = int(input())
  map = map(five,numbers)
  
if option == 6:
  map = map(six,numbers)
  
print(list(map))
