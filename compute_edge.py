import numpy as np


def compute_edge(mask):
    rsize, csize = len(mask), len(mask[0])
    edge = np.zeros((rsize, csize))
    if np.all((mask == 1)):
        return edge
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c] != 0:
                if r == 0 or c == 0 or r == len(mask)-1 or c == len(mask[0])-1:
                    edge[r][c] = 1
                    continue

                is_edge = False
                for var in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0 <= r_temp < rsize and 0 <= c_temp < csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break

                if is_edge == True:
                    edge[r][c] = 1

    return edge
