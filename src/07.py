from utils.api import get_input

input_str = get_input(7)

# WRITE YOUR SOLUTION HERE
equations = [(int(a), [int(x) for x in b.split(' ')[1:]]) for line in input_str.splitlines() for a,b in [line.split(':')]]

# part 1
res = 0
for equation_result, equation_numbers in equations:
    possible_results = [equation_numbers[0]]
    equation_numbers = equation_numbers[1:]
    while len(equation_numbers) > 0:
        possible_results = (
            [x + equation_numbers[0] for x in possible_results] +
            [x * equation_numbers[0] for x in possible_results]
        )
        equation_numbers = equation_numbers[1:]
    if equation_result in possible_results:
        res += equation_result

print(f'part 1: {res}')

# part 2
res = 0
for equation_result, equation_numbers in equations:
    possible_results = [equation_numbers[0]]
    equation_numbers = equation_numbers[1:]
    while len(equation_numbers) > 0:
        possible_results = (
            [x + equation_numbers[0] for x in possible_results] +
            [x * equation_numbers[0] for x in possible_results] +
            [int(str(x) + str(equation_numbers[0])) for x in possible_results]
        )
        equation_numbers = equation_numbers[1:]
    if equation_result in possible_results:
        res += equation_result

print(f'part 2: {res}')