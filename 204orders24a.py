import csv
file = str(input())
line = int(input())
with open("data/"+file+".csv",'r') as infile:
  read = csv.reader(infile)
  for i,v in enumerate(read):
    if i == line:
      print(f"Name: {v[0]}\nToppings: {v[1]}\nTotal: ${float(v[2]):.2f}")