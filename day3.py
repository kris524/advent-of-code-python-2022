# Basically,
# 1. split every string in half
# 2. find the common letter between them (lowercase or uppercase)
# 3. get the number of points this item has, mapping from a to z as 1 to 26
# and the mapping for capital letters as well
# just sum to total+= points got from a single string
from typing import List

with open("day3.txt") as f:
    lines = f.readlines()


res = []
for line in lines:
    res.append(line.replace("\n", ""))

# print(res)


def split_str(string: str) -> List[str]:
    length = len(string)
    string1 = string[: length // 2]
    string2 = string[length // 2 :]
    return [string1, string2]


split_str("abcdef")

common_characters = "".join(set("vJrwpWtwJgWr").intersection("hcsFMMfFFhFp"))


def get_points(letter):
    if letter.islower():

        return ord(letter) - 96
    else:
        return ord(letter) - 38
