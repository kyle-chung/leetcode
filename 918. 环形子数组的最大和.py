给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

在此处，环形数组意味着数组的末端将会与开头相连呈环状。

此外，子数组最多只能包含 A 中的每个元素一次。

示例 1：

输入：[1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

示例 2：

输入：[5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

# Kadane's algorithm
ans = cur = None
for x in A:
    cur = x + max(cur, 0)
    ans = max(ans, cur)
return ans

本题可以分为两种情况讨论

无环：最大和子数组不包含首尾元素
有环：最大和子数组包含首尾元素

无环状态下，即为 53. 最大子序和
有环状态下，要使得两端之和最大，必须让中间的子数组最小，即最后有环情况下的最大子数组和为：sum(nums)-min(middle)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)   
        max_=float('-inf')
        #无环 
        pre=0
        for i in range(n):
            pre=max(0,pre)+nums[i]
            max_=max(max_,pre)
        # 如果最子数组和小于0，说明数组中全为负数，返回最大负数即可
        if max_<0:return max_
        #有环
        pre=0
        min_=float('inf')
        for i in range(n):
            pre=min(0,pre)+nums[i]
            min_=min(min_,pre)
        
        return max(max_,sum(nums)-min_)
        

