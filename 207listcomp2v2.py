option = int(input())
values = input().split(",")
if option == 1:
  newvalues = sorted([int(x) for x in values if int(x)%4==0])
if option == 2:
  newvalues = sorted([int(x)+1 for x in values if int(x)%4==0])
if option == 3:
  first = values[0]
  newvalues = sorted([int(x) for x in values if int(x)%4==0 and int(x) < int(first)])
if option == 4:
  newvalues = sorted([x for x in values if "e" in x])
if option == 5:
  newvalues = sorted([x for x in values if "e" in x or "a" in x])
if option == 6:
  newvalues = sorted([x.upper()+"S" for x in values if "e" in x or "a" in x])
if option == 7:
  newvalues = sorted([x[-2:] if len(x) > 4 else x[:2] for x in values])
print(newvalues)