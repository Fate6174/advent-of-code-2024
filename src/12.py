from utils.api import get_input
import numpy as np

input_str = """AAAA
BBCD
BBCC
EEEC"""
input_str = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
input_str = get_input(12)

# WRITE YOUR SOLUTION HERE
garden_map = np.array([[c for c in line] for line in input_str.splitlines()])
garden_info = np.empty(garden_map.shape, dtype='object')

id = 0
idxs = np.where(garden_info == None)
while idxs[0].shape[0] > 0:
    i, j = idxs[0][0], idxs[1][0]
    plant_type = garden_map[i,j]
    neighbors_of_same_plant_type = [(i,j)]
    while neighbors_of_same_plant_type != []:
        x,y = neighbors_of_same_plant_type[0]
        if garden_info[x,y] is None:
            neighbors_2 = [
                (p,q) for p,q in [(x-1,y), (x,y+1), (x+1,y), (x,y-1)]
                    if p >= 0 and p < garden_map.shape[0] and
                    q >= 0 and q < garden_map.shape[1] and
                    garden_map[p,q] == plant_type
            ]
            fence_pieces = 4 - len(neighbors_2)
            garden_info[x,y] = (id, fence_pieces)
            neighbors_3 = [(p,q) for p,q in neighbors_2 if garden_info[p,q] is None]
            neighbors_of_same_plant_type += neighbors_3
        neighbors_of_same_plant_type = neighbors_of_same_plant_type[1:]
    idxs = np.where(garden_info == None)
    id += 1

res = 0
for i in range(id):
    region_list = [fence_pieces for id, fence_pieces in garden_info.flatten() if id == i]
    res += len(region_list) * sum(region_list)

print(f'part 1: {res}')