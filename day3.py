
# Basically,
# 1. split every string in half
# 2. find the common letter between them (lowercase or uppercase)
# 3. get the number of points this item has, mapping from a to z as 1 to 26 
# and the mapping for capital letters as well
# just sum to total+= points got from a single string

with open("day3.txt") as f:
    lines = f.readlines()


res = []
for line in lines:
    res.append(line.replace("\n", ""))

# print(res)