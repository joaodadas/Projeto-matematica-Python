import numpy as np


def transposta(m):
    rcb = list(map(lambda *i: [j for j in i], *m))
    matrix = np.array(rcb)
    print(matrix)
    