line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input('Enter your position from (A, B, C) and (1, 2, 3) in format similar to A3 or B1 or C2: ') # Where do you want to put the treasure?
letter_index = ['A', 'B', 'C']
x = letter_index.index(position[0])
y = int(position[1]) - 1
map[y][x] = 'X'
print(f"{line1}\n{line2}\n{line3}")
