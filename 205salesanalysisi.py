import csv
file = "data/"+input()+".csv"
city = input()
with open(file) as infile:
  with open("output/salesanalysis.csv",'w') as outfile:
    csvread = csv.reader(infile)
    outfile.write("City,A,B,C,D,E,Total,Average\n")
    for i,v in enumerate(csvread):
      if v[0] == city:
        total = int(v[1]) + int(v[2]) + int(v[3])+ int(v[4]) + int(v[5])
        avg = total / 5
        outfile.write(f"{v[0]},{v[1]},{v[2]},{v[3]},{v[4]},{v[5]},{total},{avg:.1f}\n")

with open("output/salesanalysis.csv") as outfile:
  for line in outfile:
    print(line,end="")