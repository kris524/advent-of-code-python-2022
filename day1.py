with open("calories.txt") as f:
    lines = f.readlines()

res = []
for line in lines:
    res.append(line.replace("\n", ""))

curr_max = 0
new_max = 0


for i in range(len(res)):
    if res[i] != "":
        curr_max += int(res[i])
    else:
        if curr_max > new_max:
            new_max = curr_max
        curr_max = 0

print(new_max)
