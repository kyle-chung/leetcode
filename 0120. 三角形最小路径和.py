给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11

解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

# dp 时间复杂度：O(n^2)，其中 n 是三角形的行数
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]
        triangle[1][0] += triangle[0][0]
        triangle[1][-1] += triangle[0][-1]
        
        pos = 2
        while pos < len(triangle):
            triangle[pos][0] += triangle[pos-1][0]
            triangle[pos][-1] += triangle[pos-1][-1]
            for i in range(1,len(triangle[pos])-1):
                triangle[pos][i] += min(triangle[pos-1][i],triangle[pos-1][i-1])
            
            pos += 1

        return min(triangle[-1])


