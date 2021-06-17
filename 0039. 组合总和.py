给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

# 回溯 时间复杂度：O(S)，其中 S 为所有可行解的长度之和
对于这类寻找所有可行解的题，我们都可以尝试用「搜索回溯」的方法来解决。

我们定义递归函数 dfs(target, combine, idx) 表示当前在 candidates 数组的第 idx 位，还剩 target 要组合，已经组合的列表为 combine
递归的终止条件为 target <= 0 或者 candidates 数组被全部用完。
那么在当前的函数中，每次我们可以选择跳过不用第 idx 个数，即执行 dfs(target, combine, idx + 1)
也可以选择使用第 idx 个数，即执行 dfs(target - candidates[idx], combine, idx)
注意到每个数字可以被无限制重复选取，因此搜索的下标仍为 idx

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx]) 
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, 0)
        return ans 
