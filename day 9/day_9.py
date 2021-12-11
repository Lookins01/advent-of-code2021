def read_input():
	with open('input.txt') as file:
		inputs = [[int(number) for number in line if number != '\n'] for line in file.readlines()]
	return inputs


def part_one(inputs):
	answer = 0
	for line_index in range(len(inputs)):
		for column_index in range(len(inputs[0])):
			adjacent_numbers = []
			hight_line = line_index - 1 if line_index > 1 else 0
			left_number = column_index - 1 if column_index > 0 else 0
			for adjacent_line in range(hight_line,line_index+2):
				for adjacent_column in range(left_number, column_index+2):
					check_line = adjacent_line == line_index
					check_column = adjacent_column == column_index
					if (adjacent_line < len(inputs) and adjacent_column < len(inputs[0])) and ((not check_line and check_column) or (check_line and not check_column)):
						adjacent_numbers.append(inputs[adjacent_line][adjacent_column])

			if min(adjacent_numbers) > inputs[line_index][column_index]:
				answer += inputs[line_index][column_index] + 1
	print('Part 1:', answer)


def part_two(inputs):
	answer = 1
	basins_sizes = []
	
	inputs = [[str(n) if n != 9 else ' ' for n in line] for line in inputs]

	for line_index in range(len(inputs)):
		for column_index in range(len(inputs[0])):
			if inputs[line_index][column_index] == ' ':
				continue
			adjacent_numbers = []
			hight_line = line_index - 1 if line_index > 1 else 0
			left_number = column_index - 1 if column_index > 0 else 0
			for adjacent_line in range(hight_line,line_index+2):
				for adjacent_column in range(left_number, column_index+2):
					check_line = adjacent_line == line_index
					check_column = adjacent_column == column_index
					if (adjacent_line < len(inputs) and adjacent_column < len(inputs[0])) and ((not check_line and check_column) or (check_line and not check_column)) and inputs[adjacent_line][adjacent_column] != ' ':
						adjacent_numbers.append([adjacent_line, adjacent_column])
			inputs[line_index][column_index] = adjacent_numbers

	def add_coords(points, acc):
		for point in points:
			y, x = point
			if [y, x] not in acc: 
				acc.append([y, x])
				add_coords(inputs[y][x], acc)
			else:
				pass

	for l in range(len(inputs)):
		for c in range(len(inputs[0])):
			if inputs[l][c] == ' ': 
				continue
			else:
				all_points = [[l, c]]
				add_coords(inputs[l][c], all_points)
				
				for point in all_points:
					y, x = point
					inputs[y][x] = ' '

				basins_sizes.append(len(all_points))

	basins_sizes.sort(reverse=True)

	for size in basins_sizes[:3]:
		answer *= size
		
	print('Part 2:', answer)


if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])
 