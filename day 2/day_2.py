def read_input():
	with open('input.txt') as file:
		inputs = [i.split() for i in file.readlines()]
	return inputs


def part_one(inputs):
	horizontal = 0
	depth = 0
	for action, value in inputs:
		value = int(value)
		if action == 'up':
			depth -= value
		elif action == 'down':
			depth += value
		elif action == 'forward':
			horizontal += value

	print('Part 1:', horizontal*depth)


def part_two(inputs):
	aim = 0
	horizontal = 0
	depth = 0
	for action, value in inputs:
		value = int(value)
		if action == 'up':
			aim -= value
		elif action == 'down':
			aim += value
		elif action == 'forward':
			horizontal += value
			depth += value * aim

	print('Part 2:', horizontal*depth)

if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])