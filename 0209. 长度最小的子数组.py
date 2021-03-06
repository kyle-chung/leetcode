给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：

输入：target = 4, nums = [1,4,4]
输出：1

# 前缀和 + 二分查找 O(nlogn)

为了使用二分查找，需要额外创建一个数组 sums 用于存储数组 nums 的前缀和
其中 sums[i] 表示从 nums[0] 到 nums[i−1] 的元素和
得到前缀和之后，对于每个开始下标 i，可通过二分查找得到大于或等于 i 的最小下标 bound，使得 sums[bound]−sums[i−1] ≥ target
并更新子数组的最小长度（此时子数组的长度是 bound−(i−1)）

因为这道题保证了数组中每个元素都为正，所以前缀和一定是递增的，这一点保证了二分的正确性

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans

在很多语言中，都有现成的库和函数来为我们实现这里二分查找(有序)大于等于某个数的第一个位置的功能
如 Python 中的 bisect.bisect_left

# sliding window O(n)
定义两个指针 start 和 end 分别表示子数组（滑动窗口窗口）的开始位置和结束位置

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans





