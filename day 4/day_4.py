def read_input():
	with open('input.txt') as file:
		inputs = [i for i in file.readlines() if i != '\n']
	return inputs


def part_one(inputs):
	numbers = [int(i) for i in inputs[0].split(',')]
	inputs = inputs[1:]
	tables = [inputs[i:i+5] for i in range(0, len(inputs), 5)]
	tables = [[i.split() for i in t] for t in tables]
	tables = [[[int(i) for i in l] for l in t] for t in tables]

	tables_win_number = {}
	for table_index in range(len(tables)):
		table_win = False
		for number_index in range(len(numbers)):
			for line_index in range(len(tables[table_index])):
				for column_index in range(len(tables[table_index][line_index])):
					if tables[table_index][line_index][column_index] == numbers[number_index]:
						tables[table_index][line_index][column_index] = None

			for line_index in range(len(tables[table_index])):
				if len(set(tables[table_index][line_index])) == 1:
					tables_win_number[table_index] = number_index
					table_win = True
					break

			if not table_win:
				for column_index in range(len(tables[table_index])):
					if len(set([o[column_index] for o in tables[table_index]])) == 1:
						tables_win_number[table_index] = number_index
						table_win = True
						break

			if table_win:
				break

	for table_index, number in tables_win_number.items():
		if number == min(tables_win_number.values()):
			win_table = table_index
			break
	sum_left_number = 0
	for line in tables[win_table]:
		sum_left_number += sum([n for n in line if n != None])
	print('Part 1:', sum_left_number*numbers[tables_win_number[win_table]])

	
def part_two(inputs):
	numbers = [int(i) for i in inputs[0].split(',')]
	inputs = inputs[1:]
	tables = [inputs[i:i+5] for i in range(0, len(inputs), 5)]
	tables = [[i.split() for i in t] for t in tables]
	tables = [[[int(i) for i in l] for l in t] for t in tables]

	tables_win_number = {}
	for table_index in range(len(tables)):
		table_win = False
		for number_index in range(len(numbers)):
			for line_index in range(len(tables[table_index])):
				for column_index in range(len(tables[table_index][line_index])):
					if tables[table_index][line_index][column_index] == numbers[number_index]:
						tables[table_index][line_index][column_index] = None

			for line_index in range(len(tables[table_index])):
				if len(set(tables[table_index][line_index])) == 1:
					tables_win_number[table_index] = number_index
					table_win = True
					break

			if not table_win:
				for column_index in range(len(tables[table_index])):
					if len(set([o[column_index] for o in tables[table_index]])) == 1:
						tables_win_number[table_index] = number_index
						table_win = True
						break

			if table_win:
				break

	for table_index, number in tables_win_number.items():
		if number == max(tables_win_number.values()):
			win_table = table_index
			break
	sum_left_number = 0
	for line in tables[win_table]:
		sum_left_number += sum([n for n in line if n != None])
	print('Part 2:', sum_left_number*numbers[tables_win_number[win_table]])


if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])
	