with open("day2.txt") as f:
    lines = f.readlines()
res = []
for line in lines:
    res.append(line.replace("\n", ""))
print(res)
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

your_shape_dict = {"X": 1, "Y": 2, "Z": 3}
other_shape_dict = {"A": 1, "B": 2, "C": 3}
outcome ={"lost": 0, "draw": 3, "won": 6}



def game(other, yours):
    points = 0
    if yours == "X": # Rock
        if other == "C": # Scissors
            points += your_shape_dict[yours] + outcome["won"]
        elif other == "B":
            points += your_shape_dict[yours] + outcome["lost"]
        else: # other == "A"
            points += your_shape_dict[yours] + outcome["draw"]

    if yours == "X":
        if other == "C":
            points += your_shape_dict[yours] + outcome["won"]
        elif other == "B":
            points += your_shape_dict[yours] + outcome["lost"]
        else: # other == "A"
            points += your_shape_dict[yours] + outcome["draw"]






# A -> Rock Y-> Paper total=8
# B -> paper X-> Rock total=1
# C -> scissors Z -> scissors total=6 
