def read_input():
	with open('input.txt') as file:
		inputs = file.read()
		inputs = [int(f) for f in inputs.split(',')]
	return inputs


def part_one(inputs):
	fuel_costs = []
	for position in range(min(inputs), max(inputs)+1):
		cost = 0
		for crab_pos in inputs:
			cost += abs(crab_pos - position)
		fuel_costs.append(cost)
		
	print('Part 1:', min(fuel_costs))

def part_two(inputs):
	fuel_costs = []
	for position in range(min(inputs), max(inputs)+1):
		cost = 0
		for crab_pos in inputs:
			cost += (0 + abs(crab_pos - position)) * (1+abs(crab_pos - position))/2
		fuel_costs.append(cost)
		
	print('Part 2:', min(fuel_costs))


if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])