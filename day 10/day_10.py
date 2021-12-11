def read_input():
	with open('input.txt') as file:
		inputs = [[symbol for symbol in line if symbol != '\n'] for line in file.readlines()]
	return inputs


def part_one(inputs):
	answer = 0
	symbol_cost = {
				   ')': 3,
				   ']': 57,
				   '}': 1197,
    			   '>': 25137
				  }
	symbols_dict = {'(': ')', '[': ']', '{': '}', '<':'>'}
	for line in inputs:
		symbols_in_line = []
		for symbol in line:
			if symbol in symbols_dict.keys():
				symbols_in_line.append(symbol)
			else:
				if symbols_dict[symbols_in_line[len(symbols_in_line)-1]] != symbol:
					answer += symbol_cost[symbol]
					break
				else:
					symbols_in_line.pop()
	print('Part 1:', answer)

def part_two(inputs):
	answer = 0
	costs = []
	symbol_cost = {
				   ')': 1,
				   ']': 2,
				   '}': 3,
    			   '>': 4
				  }
	symbols_dict = {'(': ')', '[': ']', '{': '}', '<':'>'}
	for line in inputs:
		symbols_in_line = []
		for symbol in line:
			if symbol in symbols_dict.keys():
				symbols_in_line.append(symbol)
			else:
				if symbols_dict[symbols_in_line[len(symbols_in_line)-1]] != symbol:
					break
				else:
					symbols_in_line.pop()
		else:
			if symbols_in_line != []:
				line_cost = 0
				missing_characters = [symbols_dict[o] for o in symbols_in_line[::-1]]
				for us in missing_characters:
					line_cost = (line_cost * 5) + symbol_cost[us]
			costs.append(line_cost)

	costs.sort()
	print('Part 2:', costs[int((len(costs)-1)/2)])


if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])