def summ(x):
  return sum(x) + 1

def linear(x):
  x = list(x)
  rise = x[3] - x[1]
  run = x[2] - x[0]
  if run != 0:
    slope = int(rise/run) if rise % run == 0 else rise / run
  else:
    slope = 'undefined'
  if slope != 'undefined':
    yint = -(slope*x[0]) + x[1]

  if slope != 'undefined':
    return(f'y={slope}x+{yint}' if yint != 0 and yint > 0 else f'y={slope}x{yint}' if yint != 0 and yint < 0 else f'y={slope}x')
  else:
    return('undefined')
  

option = int(input())
first = input().split(",")
second = input().split(",")
third = input().split(",")
fourth = input().split(",")
final = first

first = map(int,first)
second = map(int,second)
third = map(int,third)
fourth = map(int,fourth)
if option == 1:
  matrix = map(summ,(first,second,third,fourth))

if option == 2:
  matrix = map(linear,(first,second,third,fourth))

print(list(matrix))