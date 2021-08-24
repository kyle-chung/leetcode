给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:

输入: [1,2,3,1]
输出: true

# 无敌简单题
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(list(set(nums))) < len(nums)
