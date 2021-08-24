给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
  
# haspmap O(n)

遍历数组：

若nums[i]不在hash中，则令nums[i]为key，value为当前的索引i

若已存在：
判断当前的索引和上一相同元素的索引差是否小于等于k。若满足，返回TrueTrue。
将索引更新为当前索引，hash[nums[i]]=i

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        for i in range(len(nums)):
            if(nums[i] not in hash):
                hash[nums[i]]=i
            else:
                if(i-hash[nums[i]]<=k):
                    return True
                else:
                    hash[nums[i]]=i
        return False

