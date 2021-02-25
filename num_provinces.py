"""NumOfProvinces LeetCode solution."""


class Solution:
    """
    Given an adjacency matrix, find the number of provinces.

    Each node represents a "city". A city with an edge to another
    city is directly connected, while a city connected to another
    node by two edges is indirectly connected. A group of directly or
    indirectly connected cities is called a province.

    Return value:int
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        numOfProvinces = 0
        visited = set()

        for start in range(len(isConnected)):
            if start not in visited:
                numOfProvinces += 1
                dfs(start)

        return numOfProvinces
