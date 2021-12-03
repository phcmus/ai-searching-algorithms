from queue import PriorityQueue
from Utils.PointUtils import *

def best_first_search(map, source, target):
    # source = (x, y)
    # target = (x, y)

    ksource = PointUtils.k(source[0], source[1], map.col)
    kend = PointUtils.k(target[0], target[1], map.col)

    n = map.row * map.col
    cost = 0
    res = []
    visited = [0] * n
    visited[0] = True
    pq = PriorityQueue()
    pq.put((0, ksource))
    while pq.empty() == False:
        u = pq.get()[1]
        res.append((u // map.col, u % map.col))
        cost += map.cost(u)
        if u == kend:
            break
        for v, c in map.roadmap[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))

    # res = [(), (), ()...]
    # cost = int
    return res, cost