with open("./waybacks", "r") as file:
    all = file.readlines()

new = []
for i in range(len(all)):
    if all[i] == "" or all[i] == "\n":
        print(i)
    else:
        new.append(all[i])

with open("wb0san", "w") as file:
    for i in new:
        file.write(i)
