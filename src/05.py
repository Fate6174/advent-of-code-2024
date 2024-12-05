from utils.api import get_input

input_str = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
# input_str = get_input(5)

# WRITE YOUR SOLUTION HERE
sep_idx = input_str.find('\n\n')
rules = [(int(item[:2]), int(item[3:])) for item in input_str[:sep_idx].splitlines()]
updates = [[int(x) for x in item.split(',')] for item in input_str[sep_idx+2:].splitlines()]

def sort_rules(l : list[tuple[int,int]]) -> list[int]:
    

print(rules)
# print(updates)

# part 1
def match_safe(l : list[int]) -> int:
    for i in range(len(l)):
        for j in range(i):
            for rule in rules:
                a, b = rule
                if l[j] == b and l[i] == a:
                    return 0
        for j in range(i+1,len(l)):
            for rule in rules:
                a, b = rule
                if l[j] == a and l[i] == b:
                    return 0
    return l[len(l) // 2]

res = sum([match_safe(update) for update in updates])
print(f'part1: {res}')

# part 2
