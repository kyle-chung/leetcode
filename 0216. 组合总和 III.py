找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 

示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
  
# backtrack 如何剪枝是关键
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < 6: return []
        res = []
        def backtrack(num, path, k, n):
            if k == 0 and n == 0:
                res.append(path[:])
            if n < 0 or k < 0:
                return 
            for cn in range(num, 10):
                if cn > n:
                    break
                path.append(cn)
                backtrack(cn+1, path, k-1, n-cn)
                path.pop()
            return 

        backtrack(1, [], k, n)
        return res
  
  
  
