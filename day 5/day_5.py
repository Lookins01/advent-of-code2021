def read_input():
	with open('input.txt') as file:
		inputs = [[i.split(',') for i in line.replace('\n', '').split('->')] for line in file.readlines()]
		for line in range(len(inputs)):
			for couple in range(len(inputs[line])):
				for number in range(len(inputs[line][couple])):
					inputs[line][couple][number] = int(inputs[line][couple][number])
	return inputs


def part_one(inputs):
	field_x_size = max([max([o[0] for o in i]) for i in inputs]) + 1
	field_y_size = max([max([o[1] for o in i]) for i in inputs]) + 1
	field_sise = field_y_size * field_x_size
	field = [[0 for _ in range(field_x_size)] for _ in range(field_y_size)]
	
	for first_cords, second_cords in inputs:
		if first_cords[0] != second_cords[0] and first_cords[1] != second_cords[1]:
			# 8,0 -> 0,8
			continue

		elif first_cords[0] == second_cords[0] and first_cords[1] == second_cords[1]:
			field[first_cords[0]][first_cords[1]] += 1
		
		elif first_cords[0] == second_cords[0]:
			# 1,2 -> 1,5
			for i in range(min(first_cords[1], second_cords[1]), max(first_cords[1], second_cords[1]) + 1):
				field[i][first_cords[0]] += 1
		
		elif first_cords[1] == second_cords[1]:
			# 2,3 -> 4,3
			for i in range(min(first_cords[0], second_cords[0]), max(first_cords[0], second_cords[0]) + 1):
				field[first_cords[1]][i] += 1
	
	count_of_save_points = 0
	for line in field:
		for column in line:
			if column >= 2:
				count_of_save_points += 1

	print('Part 1:', count_of_save_points)

def part_two(inputs):
	field_x_size = max([max([o[0] for o in i]) for i in inputs]) + 1
	field_y_size = max([max([o[1] for o in i]) for i in inputs]) + 1
	field_sise = field_y_size * field_x_size
	field = [[0 for _ in range(field_x_size)] for _ in range(field_y_size)]
	
	for first_cords, second_cords in inputs:
		if first_cords[0] != second_cords[0] and first_cords[1] != second_cords[1]:
			# 8,0 -> 0,8
			now_cords = first_cords[:]
			while now_cords[0] != second_cords[0] - 1*(second_cords[0]<first_cords[0]) + 1*(second_cords[0]>first_cords[0]):
				field[now_cords[1]][now_cords[0]] += 1

				if first_cords[0] > second_cords[0]:
					now_cords[0] -= 1
				elif first_cords[0] < second_cords[0]:
					now_cords[0] += 1

				if first_cords[1] > second_cords[1]:
					now_cords[1] -= 1
				elif first_cords[1] < second_cords[1]:
					now_cords[1] += 1

		elif first_cords[0] == second_cords[0] and first_cords[1] == second_cords[1]:
			field[first_cords[0]][first_cords[1]] += 1
		
		elif first_cords[0] == second_cords[0]:
			# 1,2 -> 1,5
			for i in range(min(first_cords[1], second_cords[1]), max(first_cords[1], second_cords[1]) + 1):
				field[i][first_cords[0]] += 1
		
		elif first_cords[1] == second_cords[1]:
			# 2,3 -> 4,3
			for i in range(min(first_cords[0], second_cords[0]), max(first_cords[0], second_cords[0]) + 1):
				field[first_cords[1]][i] += 1
	
	count_of_save_points = 0
	for line in field:
		for column in line:
			if column >= 2:
				count_of_save_points += 1

	print('Part 2:', count_of_save_points)


if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])