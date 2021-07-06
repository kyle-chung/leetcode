给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

# backtrack求过易懂框架版
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if len(track) == k:
            result.append(track[:])
        for i in range(start, n+1):
            track.append(i)
            self.backtrack(n, k, i+1, track, result)
            track.pop()
            
# backtrack剪枝版            
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if k == 0:
            result.append(track[:])
            return
        for i in range(start, n-k+2):
            track.append(i)
            self.backtrack(n, k-1, i+1, track, result)
            track.pop()
