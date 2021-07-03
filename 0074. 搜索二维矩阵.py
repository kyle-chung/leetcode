编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 
示例 1：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

# 二分
若将矩阵每一行拼接在上一行的末尾，则会得到一个升序数组，我们可以在该数组上二分找到目标元素

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = len(matrix)
        row = len(matrix[0])
        left = 0
        right = line * row
        while left < right:
            i, j = divmod((left + right) // 2, row) # 如果参数 a 与 参数 b 都是整数，函数返回的结果相当于 (a // b, a % b)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = i * row + j + 1
            else:
                right = i * row + j
        return False
