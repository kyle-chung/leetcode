一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2

解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        temp = [[0]*n for _ in range(m)]
#       改变原有地图矩阵
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                temp[0][j] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                temp[i][0] = 1
            else:
                break
#       开始dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[-1][-1]


      
