with open ('The First Puzzle Input.txt') as Input:
	Inputs = Input.readlines ()
	Inputs = [int (Input.strip ("\n")) for Input in Inputs]

Previous, Answer = Inputs [0], 0
for Number in Inputs [1:]:
	if Number > Previous:
		Answer += 1
	Previous = Number

print (f'The First Puzzle Answer is {Answer}')