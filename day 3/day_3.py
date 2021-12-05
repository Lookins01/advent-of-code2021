def read_input():
	with open('input.txt') as file:
		inputs = [[j for j in i if j != '\n'] for i in file.readlines()]
	return inputs


def part_one(inputs):
	gamma_rate = [0 for _ in inputs[0]]
	epsilon_rate = [0 for _ in inputs[0]]
	zeros = 0
	ones = 0
	for j in range(len(inputs[0])):
		for i in range(len(inputs)):
			if int(inputs[i][j]) == 0:
				zeros += 1
			elif int(inputs[i][j]) == 1:
				ones += 1

		gamma_rate[j] = 0 if zeros < ones else 1
		epsilon_rate[j] = 0 if zeros > ones else 1
		zeros = 0
		ones = 0

	gamma_rate = int(''.join([str(o) for o in gamma_rate]), 2)
	epsilon_rate = int(''.join([str(o) for o in epsilon_rate]), 2)
	print('Part 1:', gamma_rate * epsilon_rate)



def part_two(inputs):
	oxygen_generator_rate = [0 for _ in inputs[0]]
	co2_scrubber_rate = [0 for _ in inputs[0]]


	# Calculate oxygen genarator rate
	zeros = 0
	ones = 0
	correct_inputs = inputs[:]
	for j in range(len(correct_inputs[0])):
		for i in range(len(correct_inputs)):
			if int(correct_inputs[i][j]) == 0:
				zeros += 1
			elif int(correct_inputs[i][j]) == 1:
				ones += 1
		if zeros <= ones:
			correct_inputs = [n for n in correct_inputs if int(n[j]) == 1]
		else:
			correct_inputs = [n for n in correct_inputs if int(n[j]) == 0]
		if len(correct_inputs) == 1:
			oxygen_generator_rate = correct_inputs[0]
			break
		zeros = 0
		ones = 0

	# Calculate CO2 scrubber rate
	zeros = 0
	ones = 0
	correct_inputs = inputs[:]
	for j in range(len(correct_inputs[0])):
		for i in range(len(correct_inputs)):
			if int(correct_inputs[i][j]) == 0:
				zeros += 1
			elif int(correct_inputs[i][j]) == 1:
				ones += 1
		if zeros > ones:
			correct_inputs = [n for n in correct_inputs if int(n[j]) == 1]
		else:
			correct_inputs = [n for n in correct_inputs if int(n[j]) == 0]

		if len(correct_inputs) == 1:
			co2_scrubber_rate = correct_inputs[0]
			break

		zeros = 0
		ones = 0

	oxygen_generator_rate = int(''.join([str(o) for o in oxygen_generator_rate]), 2)
	co2_scrubber_rate = int(''.join([str(o) for o in co2_scrubber_rate]), 2)
	print('Part 2:', oxygen_generator_rate * co2_scrubber_rate)

if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])
	