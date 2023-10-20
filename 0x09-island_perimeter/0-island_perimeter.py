#!/usr/bin/python3
'''Island Perimeter'''


def island_perimeter(grid):
    '''ouputs the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    lst_max = len(grid[0]) - 1  # index of the last square in list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right side of island
                if land_idx == 0:
                    # left side of island
                    counter += 1

                    # right side of island
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # left side of island
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side island
                    counter += 1
                else:
                    # left side island
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side island
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # top and down of island
                if lst_idx == 0:
                    # top side island
                    counter += 1

                    # bottom side island
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # top side island
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side island
                    counter += 1
                else:
                    # top side island
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side island
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
