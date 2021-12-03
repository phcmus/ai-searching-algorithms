from sys import argv

from uniformed_search_map import uniformed_search_map
from Utils.PointUtils import *
from visualize_maze import visualize_maze

script, filename = argv

def depth_first_search(map, source, target):
    visited = [False] * map.col * map.row
    parent = [-1] * map.col * map.row
    open = [source]
    visited[PointUtils.k(source[0], source[1], map.col)] = True # set start = visited
    result = []
    while open:
        item = open.pop(0) # open : list of point (x,y) => item = (x,y)
        if item == target:
            # parent traversal
            while parent[PointUtils.k(item[0], item[1], map.col)] != -1:
                k_parent = parent[PointUtils.k(item[0], item[1], map.col)]
                result.insert(0, item)
                item = (k_parent // map.col, k_parent % map.col)
            result.insert(0, source)
            break
        else:
            # map.roadmap[k] = list (k, cost) => i = (k, cost)
            # item's child list traversal
            # current_parrent = item
            for i in map.roadmap[PointUtils.k(item[0], item[1], map.col)]:
                if visited[i[0]] == False:
                    open.insert(0, (i[0] // map.col, i[0] % map.col))
                    visited[i[0]] = True
                    parent[i[0]] = PointUtils.k(item[0], item[1], map.col)

    return result

def main():
    # config maze
    map = uniformed_search_map(filename)
    print('Start building roadmap')
    map.build_roadmap()
    print('Done building roadmap')

    # start searching
    sstart = map.get_start()
    eend = map.get_end()
    result = depth_first_search(map, sstart, eend)
    
    # print result
    if len(result) != 0 and (result[0] == sstart) and (result[-1] == eend):
        print('The road from ', sstart, 'to', eend, 'is: ', result, '. Cost = ', len(result))
    else:
        print('Cannot find the road from ', sstart, 'to', eend)
        return

    bonus_point = [(o.x, o.y, o.point) for o in map.awards]
    
    visualize_maze(map.graph, bonus_point, map.get_start(), map.get_end(), result)

main()