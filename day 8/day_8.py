def read_input():
	with open('input.txt') as file:
		inputs = file.readlines()
		inputs = [[o.split() for o in line.split('|')] for line in inputs]
	return inputs


def check(lst, sub_lst):
	return set(sub_lst).issubset(lst)


def part_one(inputs):
	answer = 0
	for _, display in inputs:
		for d in display:
			if len(d) in [2, 3, 4, 7]:
				answer += 1 
	print('Part 1:', answer)


def part_two(inputs):

	answer = 0
	for numbers_paterns, numbers in inputs:
		number_dict = {} # {1: ab, 4: avsd, ...}
		while len(number_dict.keys()) != 10:
			for number_patern in numbers_paterns:
				if len(number_patern) == 2 and not number_dict.get(1):
					number_dict[1] = number_patern
				elif len(number_patern) == 4 and not number_dict.get(4):
					number_dict[4] = number_patern
				elif len(number_patern) == 3 and not number_dict.get(7):
					number_dict[7] = number_patern
				elif len(number_patern) == 7 and not number_dict.get(8):
					number_dict[8] = number_patern
				elif len(number_patern) == 6 and number_dict.get(1):
					if not check(number_patern, number_dict[1]):
						number_dict[6] = number_patern
					elif number_dict.get(4) and number_dict.get(1) and check(number_patern, set(number_dict[4]).symmetric_difference(number_dict[1])):
						number_dict[9] = number_patern
					elif number_dict.get(9):
						number_dict[0] = number_patern
				elif len(number_patern) == 5 and number_dict.get(1):
					if check(number_patern, number_dict[1]):
						number_dict[3] = number_patern
					elif number_dict.get(9) and check(number_dict[9], number_patern):
						number_dict[5] = number_patern
					elif number_dict.get(3) and number_dict.get(5):
						number_dict[2] = number_patern
		
		number_dict = {i: set(number_dict[i]) for i in number_dict}
		output_number = ['']*4
		i = 0
		for number in numbers:
			for n in number_dict:
				if set(number) == set(number_dict[n]):
					output_number[i] = str(n)
			i += 1

		answer += int(''.join(output_number))

	print('Part 2:', answer)

if __name__ == '__main__':
	inputs = read_input()
	part_one(inputs[:])
	part_two(inputs[:])
	