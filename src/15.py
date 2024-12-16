from utils.api import get_input
import numpy as np

input_str = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
input_str = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
input_str = get_input(15)

# WRITE YOUR SOLUTION HERE

# part 1
map, directions = input_str.split('\n\n')

map = np.array([[c for c in line] for line in map.splitlines()])
robot_pos = np.concatenate(np.where(map == '@'))

directions = ''.join(directions.splitlines())

for direction in directions:
    match direction:
        case '^': step = np.array([-1,0])
        case '>': step = np.array([0,1])
        case 'v': step = np.array([1,0])
        case '<': step = np.array([0,-1])
    
    if map[*(robot_pos+step)] == '.':
        map[*(robot_pos)] = '.'
        map[*(robot_pos+step)] = '@'
        robot_pos += step
    elif map[*(robot_pos+step)] == 'O':
        k = 1
        while True:
            k += 1
            if map[*(robot_pos+k*step)] == '.':
                map[*(robot_pos)] = '.'
                map[*(robot_pos+step)] = '@'
                for j in range(2,k+1):
                    map[*(robot_pos+j*step)] = 'O'
                robot_pos += step
                break
            elif map[*(robot_pos+k*step)] == 'O':
                continue
            else:
                break

res = sum([100*i + j for i,j in zip(*np.where(map == 'O'))])
print(f'part 1: {res}')

# part 2
# map, directions = input_str.split('\n\n')

# map = np.array([['##' if c == '#' else ('..' if c == '.' else ('[]' if c == 'O' else '@.')) for c in line] for line in map.splitlines()])
# robot_pos = np.concatenate(np.where(map == '@'))

# directions = ''.join(directions.splitlines())

# for direction in directions:
#     match direction:
#         case '^': step = np.array([-1,0])
#         case '>': step = np.array([0,1])
#         case 'v': step = np.array([1,0])
#         case '<': step = np.array([0,-1])
    
#     if map[*(robot_pos+step)] == '.':
#         map[*(robot_pos)] = '.'
#         map[*(robot_pos+step)] = '@'
#         robot_pos += step
#     elif map[*(robot_pos+step)] == 'O':
#         k = 1
#         while True:
#             k += 1
#             if map[*(robot_pos+k*step)] == '.':
#                 map[*(robot_pos)] = '.'
#                 map[*(robot_pos+step)] = '@'
#                 for j in range(2,k+1):
#                     map[*(robot_pos+j*step)] = 'O'
#                 robot_pos += step
#                 break
#             elif map[*(robot_pos+k*step)] == 'O':
#                 continue
#             else:
#                 break

# print(map)
# res = sum([100*i + j for i,j in zip(*np.where(map == 'O'))])
# print(f'part 1: {res}')