import heapq

class Solution(object):
        def kClosest(self, points, k):
            return nsmallest(k, points, lambda (x, y): x * x + y * y)
