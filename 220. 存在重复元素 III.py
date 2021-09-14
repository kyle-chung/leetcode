给你一个整数数组 nums 和两个整数 k 和 t 
请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。

示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

# 滑动窗口 & 二分 
每次遍历到任意位置 i 的时候，往后检查 k 个元素，但这样做的复杂度是 O(nk) 的，会超时

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False
      
时间复杂度：TreeSet 基于红黑树，查找和插入都是 O(logk) 复杂度。整体复杂度为 O(nlogk)


      
      
      
      
      
      
