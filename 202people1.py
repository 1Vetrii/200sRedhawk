string = input()
strings = []
while string != "q":

  table = string.split(",")
  strings.append(f'{table[0]},"{table[1]}, {table[2]}",{table[3]}'+"\n")
  string = input()
with open("output/addresses.csv","w") as outfile:
  outfile.write("".join(strings))

with open("output/addresses.csv") as infile:
  for line in infile:
    print(line,end="")