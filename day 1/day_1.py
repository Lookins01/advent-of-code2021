def read_input():
	with open('input.txt') as file:
		inputs = [int(i) for i in file.readlines()]
	return inputs


def part_one(inputs):
	previos = None
	result = 0
	for i in inputs:
		if previos and i > previos:
			result += 1
		previos = i

	print("Part 1:", result)


def part_two(inputs):
	sum_prev = None
	sum_now = 0
	result = 0
	for i in range(len(inputs)):
		sum_now = sum(inputs[i:i+3])
		if sum_prev and sum_now > sum_prev:
			result += 1
		sum_prev = sum_now
	print("Part 2:", result)


if __name__ == "__main__":
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])
