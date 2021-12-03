from abc import abstractmethod
from Utils.PointUtils import *
from Models.award import *

class Map:
    row = 0
    col = 0
    road_char = ' '
    start_char = 'S'
    award_char = '+'
    awards = []
    graph = [] # matrix of maze
    roadmap = [[] for i in range(row * col)] # map of connection
    
    def __init__(self, f):
        with open(f, 'r') as inputfile:
            # nap award
            award_count = int(inputfile.readline())
            while award_count > 0:
                aaward = inputfile.readline()
                self.awards.append(award(int(aaward.split(' ')[0]), int(aaward.split(' ')[1]), int(aaward.split(' ')[2])))
                award_count -= 1

            # nap map
            for line in inputfile.read().splitlines():
                self.graph.append(list(line))
            self.row = len(self.graph)
            self.col = len(self.graph[0])

    def build_roadmap(self):
        print('Map have ', self.row, 'rows and ', self.col, 'columns.')
        self.roadmap = [[] for i in range(self.row * self.col)]
        for i in range(self.row):
            for j in range(self.col):
                self.find_neighbor((i, j))
        self.find_neighbor(self.get_start())
        self.find_neighbor(self.get_end())
        for i in self.awards:
            self.find_neighbor((i.x, i.y))
    
    @abstractmethod
    def cost(self, x):
        pass

    def addedge(self, x, y, cost):
        # add a road from x to y
        # costx is cost when choose to go to y from x => x->y costx
        # costy is cost when choose to go to x from y => y->x costy
        # if cost is the road from x to y, costx = costy = xy        
        if (y, cost(y)) not in self.roadmap[x]: self.roadmap[x].append((y, cost(y)))
        if (x, cost(x)) not in self.roadmap[y]: self.roadmap[y].append((x, cost(x)))

    def find_neighbor(self, point):
        if self.graph[point[0]][point[1]] != self.road_char and self.graph[point[0]][point[1]] != self.start_char:
            return
            
        if point[0] > 0:
            if self.graph[point[0] - 1][point[1]] == self.road_char:
                self.addedge(
                    PointUtils.k(point[0], point[1], self.col), 
                    PointUtils.k(point[0] - 1, point[1], self.col),
                    self.cost)

        if point[0] < self.row - 1:
            if self.graph[point[0] + 1][point[1]] == self.road_char:
                self.addedge(
                    PointUtils.k(point[0], point[1], self.col), 
                    PointUtils.k(point[0] + 1, point[1], self.col),
                    self.cost)

        if point[1] > 0:
            if self.graph[point[0]][point[1] - 1] == self.road_char:
                self.addedge(
                    PointUtils.k(point[0], point[1], self.col), 
                    PointUtils.k(point[0], point[1] - 1, self.col),
                    self.cost)

        if point[1] < self.col - 1:
            if self.graph[point[0]][point[1] + 1] == self.road_char:
                self.addedge(
                    PointUtils.k(point[0], point[1], self.col), 
                    PointUtils.k(point[0], point[1] + 1, self.col),
                    self.cost)
        
    def get_start(self):
        for i in self.graph:
            if i.count(self.start_char) > 0:
                return (self.graph.index(i), i.index(self.start_char))
    
    def get_end(self):
        if self.row == 0 or self.col == 0:
            pass
        else:
            for i in range(self.row):
                if self.graph[i][0] == self.road_char:
                    return (i, 0)
                elif self.graph[i][self.col - 1] == self.road_char:
                    return (i, self.col - 1)

                for i in range(self.col):
                    if self.graph[0][i] == self.road_char:
                        return (0, i)
                    elif self.graph[self.row - 1][i] == self.road_char:
                        return (self.row - 1, i)