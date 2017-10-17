# coding: utf-8

import numpy as np


##############################################
#                                            #
#      |   | 1  | 2  | 3  | 4  | 5 | 6  |    #
#      |---|----|----|----|----|---|----|    #
#      | 1 | 0  | 7  | 9  | Z  | Z | 14 |    #
#      | 2 | 7  | 0  | 10 | 15 | Z | Z  |    #
#      | 3 | 9  | 10 | 0  | 11 | Z | 2  |    #
#      | 4 | Z  | 15 | 11 | 0  | 6 | Z  |    #
#      | 5 | Z  | Z  | Z  | 6  | 0 | 9  |    #
#      | 6 | 14 | Z  | 2  | Z  | 9 | 0  |    #
#                                            #
##############################################


Graph = [[0, 7, 9, np.Inf, np.Inf, 14],
         [7, 0, 10, 15, np.Inf, np.Inf],
         [9, 10, 0, 11, np.Inf, 2],
         [np.Inf, 15, 11, 0, 6, np.Inf],
         [np.Inf, np.Inf, np.Inf, 6, 0, 9],
         [14, np.Inf, 2, np.Inf, 9, 0]]


result = [np.Inf, np.Inf, np.Inf, np.Inf, np.Inf, np.Inf]
reversed = [0, 1, 2, 3, 4, 5]
S = []


def dijkstra(A, B):
    S.append(A)
    reversed.remove(A)
    result[A] = 0
    while reversed:
        for i in reversed:
            tmp = Graph[S[-1]][i] + result[S[-1]]
            if tmp < result[i]:
                result[i] = tmp
        min_var, idx = np.Inf, -1
        for i in reversed:
            if result[i] < min_var:
                min_var = result[i]
                idx = i
        reversed.remove(idx)
        S.append(idx)

    return result[B]


if __name__ == "__main__":
    print dijkstra(0, 3)
