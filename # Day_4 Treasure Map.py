# Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map =  [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?")

x = position[0]                     # x >> vertical axis
y = position[1]                     # y >> Horizontal axis

selected_row = map[int(x) - 1]
selected_row[int(y) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
