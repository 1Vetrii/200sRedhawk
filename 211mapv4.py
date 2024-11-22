c = -1
c2 = -1
def one(x):
  return len(x)

def two(x):
  return x+"!"

def three(x):
  return x[::-1].lower()

def four(x):
  global c
  c+=1
  return x[0]+y[c][-1]

def five(x):
  global c
  c += 1
  return int(x+y[c]+z[c])

def six(x):
  global c2
  c2 += 1
  return int(x)**int(y[c2])

option = int(input())
inp = input()

if option == 1:
  inp = inp.split()
  map = map(one,inp)

if option == 2:
  inp = inp.split()
  map = map(two,inp)

if option == 3:
  inp = inp.split()
  map = map(three,inp)

if option == 4:
  inp = inp.split()
  y = input().split()
  map = map(four,inp)

if option == 5:
  inp = inp.split(",")
  y = input().split(",")
  z = input().split(",")
  map = map(five,inp)

if option == 6:
  inp = inp.split(",")
  y = input().split(",")
  map = map(six,inp)

print(list(map))
  

  