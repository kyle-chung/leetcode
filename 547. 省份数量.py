有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

示例 1：

输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

示例 2：

输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3

# BFS 时间复杂度：O(n^2)  空间复杂度：O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0
        
        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1
        
        return circles

# DFS 时间复杂度：O(n^2) 空间复杂度：O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        
        return circles
      
# 并查集 时间复杂度：O(n^2 * log n) 空间复杂度：O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)
        
        provinces = len(isConnected)
        parent = list(range(provinces))
        
        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        circles = sum(parent[i] == i for i in range(provinces))
        return circles


基本概念

并查集是一种数据结构
并查集这三个字，一个字代表一个意思。
并（Union），代表合并
查（Find），代表查找
集（Set），代表这是一个以字典为基础的数据结构，它的基本功能是合并集合中的元素，查找集合中的元素
并查集的典型应用是有关连通分量的问题
并查集解决单个问题（添加，合并，查找）的时间复杂度都是O(1)O(1)
因此，并查集可以应用到在线算法中

