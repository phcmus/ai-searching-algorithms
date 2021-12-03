from sys import argv
from queue import PriorityQueue

from Models.Map import Map, abstractmethod
from Utils.PointUtils import *
from visualize_maze import visualize_maze
from best_first_search import best_first_search

class greedy_best_first_search_map(Map):
    def cost(self, k):
        k_row = k//self.col
        k_col = k%self.col
        return PointUtils.distance((k_row, k_col), self.get_end())

script, filename = argv

def main():
    # config maze 
    map = greedy_best_first_search_map(filename)
    print('Start building roadmap')
    map.build_roadmap()
    print('Done building roadmap')

    # start searching
    sstart = map.get_start()
    eend = map.get_end()
    result, cost = best_first_search(map, sstart, eend)

    # print result
    if len(result) != 0 and (result[0] == sstart) and (result[-1] == eend):
        print('The road from', sstart, 'to', eend, 'is:', result, '. Cost = ', cost, '.')
    else:
        print('Cannot find the road from ', sstart, 'to', eend, '.')
        return

    bonus_point = [(o.x, o.y, o.point) for o in map.awards]
    
    visualize_maze(map.graph, bonus_point, map.get_start(), map.get_end(), result)

main()