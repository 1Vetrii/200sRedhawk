a = int(input())

names = []

for i in range(a):
  name = input()
  names.append(name)
game1 = []
game2 = []
game3 = []
for game in range(3):
  for i in range(a):
    pointsearned = int(input())
    if game == 0:
      game1.append(pointsearned)
    if game == 1:
      game2.append(pointsearned)
    if game == 2:
      game3.append(pointsearned)

with open("output/scores.csv","w") as outfile:
  for i in range(len(names)):
    outfile.write(names[i]+","+str(game1[i])+","+str(game2[i])+","+str(game3[i])+"\n")

with open("output/scores.csv") as outfile:
  for line in outfile:
    print(line,end="")