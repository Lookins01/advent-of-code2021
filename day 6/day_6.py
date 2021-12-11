def read_input():
	with open('input.txt') as file:
		inputs = file.read()
		inputs = [int(f) for f in inputs.split(',')]
	return inputs


def part_one(inputs):
	days = 0
	while days < 80:
		for fish_index in range(len(inputs)):
			if inputs[fish_index] > 0:
				inputs[fish_index] = inputs[fish_index] - 1
			else:
				inputs[fish_index] = 6
				inputs.append(8)
		days += 1
	print('Part 1:', len(inputs))


def part_two(inputs):
	# Index in list equals left days
	# [1, 2, 3, 4, 5, 6, 5, 4, 2] -> [2, 3, 4, 5, 6, 5, 5, 2, 1]
	fish_dict = {}
	for fish in inputs:
		if fish not in fish_dict:
			fishs = [0]*9
			fishs[fish] += 1
			days = 0
			while days < 256:
				fishs_copy = fishs
				fishs = [0]*9
				for fish_index in range(len(fishs)):
					if fish_index == 0:
						fishs[8] = fishs_copy[0]
						fishs[6] += fishs_copy[0] + fishs_copy[7]
					elif fish_index != 7:
						fishs[fish_index-1] = fishs_copy[fish_index]
				days += 1
			fish_dict[fish] = sum(fishs)

	answer = 0
	for fish in inputs:
		answer += fish_dict[fish]
	print('Part 2:', answer)


if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])
