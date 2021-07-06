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

重点概括：

如果解决一个问题有多个步骤，每一个步骤有多种方法，题目又要我们找出所有的方法，可以使用回溯算法；
回溯算法是在一棵树上的 深度优先遍历（因为要找所有的解，所以需要遍历）；
组合问题，相对于排列问题而言，不计较一个组合内元素的顺序性（即 [1, 2, 3] 与 [1, 3, 2] 认为是同一个组合）
因此很多时候需要按某种顺序展开搜索，这样才能做到不重不漏。
回溯算法首先需要画出递归树，不同的树决定了不同的代码实现。下面给出了两种画树的思路

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
