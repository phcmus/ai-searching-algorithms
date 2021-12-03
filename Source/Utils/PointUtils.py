import math

class PointUtils:
    @staticmethod
    def k(krow, kcol, col):
        return krow * col + kcol

    @staticmethod
    def distance(point1, point2):
        return math.sqrt(((point1[0] - point2[0])**2)+((point1[1] - point2[1])**2))