给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# 直接从后遍历，遇到一个数就把所有子集加上该数组成新的子集
class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in range(len(nums)-1, -1, -1):
            for subres in res[:]: res.append(subres+[nums[i]])
    
        return res
    
注意代码中res[:]是必须的，因为切片是引用新的对象，此时在循环中res[:]是不更新的
而res是不断有元素push进去的，很trick

# backtracking
