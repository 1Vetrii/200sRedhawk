string = input()
strings = []
with open("data/"+string+".csv") as infile:
  for line in infile:
      table = line.strip().split(",")
      table = [x.strip('"').strip("”").strip("“") for x in table]
      strings.append(f'{table[1]} is the address of {table[0]} who is {table[3]} years old'+"\n")
print("".join(strings).strip())