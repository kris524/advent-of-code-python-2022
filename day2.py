with open("day2.txt") as f:
    lines = f.readlines()
res = []
for line in lines:
    res.append(line.replace("\n", ""))
# print(res)
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

your_shape_dict = {"X": 1, "Y": 2, "Z": 3}
other_shape_dict = {"A": 1, "B": 2, "C": 3}
outcome ={"lost": 0, "draw": 3, "won": 6}



def play(other, yours):
    points = 0
    if yours == "X": # Rock
        if other == "C": # Scissors
            points += your_shape_dict[yours] + outcome["won"]
        elif other == "B": #Paper
            points += your_shape_dict[yours] + outcome["lost"]
        else: # other == "A" # Rock
            points += your_shape_dict[yours] + outcome["draw"]

    if yours == "Y": #Paper
        if other == "C": # Scissors 
            points += your_shape_dict[yours] + outcome["lost"]
        elif other == "A": #Rock
            points += your_shape_dict[yours] + outcome["won"]
        else: # other == "A"
            points += your_shape_dict[yours] + outcome["draw"]

    if yours == "Z": #Scissors
        if other == "A": # Rock 
            points += your_shape_dict[yours] + outcome["lost"]
        elif other == "B": #Paper
            points += your_shape_dict[yours] + outcome["won"]
        else: # other == "A"
            points += your_shape_dict[yours] + outcome["draw"]
    return points

# Test
# res = ["A Y", "B X", "C Z"]

final_points = 0
for game in res:
    entries = game.split()
    final_points += play(entries[0], entries[1])

print(final_points)



# A -> Rock Y-> Paper total=8
# B -> paper X-> Rock total=1
# C -> scissors Z -> scissors total=6 
