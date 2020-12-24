n = int(input("Enter a number : "))

space_AB = n - 1
space_inside = -1
part_one = n

for row in range(part_one):
	txt = ""
	for space_A_do in range(space_AB):
		txt += "A"

	txt += "+"

	for space_inside_do in range(space_inside):
		txt += "E"

	if row > 0:
		txt += "+"

	for space_B_do in range(space_AB):
		txt += "B"

	space_AB -= 1
	space_inside += 2
	print(txt)


space_CD = 1
part_two = n - 1
space_inside -= 4

for row in range(part_two):
        txt = ""
        for space_C_do in range(space_CD):
                txt += "C"

        txt += "+"

        for space_inside_do in range(space_inside):
                txt += "E"

        if row < (part_two - 1):
                txt += "+"

        for space_D_do in range(space_CD):
                txt += "D"

        space_CD += 1
        space_inside -= 2
        print(txt)