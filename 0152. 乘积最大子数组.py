给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
  
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# dp
那么根据「53. 最大子序和」的经验，我们这里维护两个数，dp_max, dp_min

考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正
并且我们希望这个积尽可能「负得更多」，即尽可能小

如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大

class Solution:
    def maxProduct(nums):
        dp_max, dp_min = nums[0],nums[0] 
        maxp = nums[0]
        for i in range(1,len(nums)):
            # 　注意 这里必须是同时更新
            dp_max, dp_min = max(nums[i], dp_max*nums[i], dp_min*nums[i]), min(nums[i], dp_max*nums[i], dp_min*nums[i])
            maxp = max(maxp, dp_max)
        return maxp
