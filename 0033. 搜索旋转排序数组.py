整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k 上进行了 旋转

例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

# 二分
将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。如此循环.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:  # 如果中间值是目标，直接返回
                return mid
            if nums[mid] < nums[right]:  # 证明 mid 到 right 之间是升序的
                if nums[mid] < target <= nums[right]:  # 如果 target 在这个升序区间内
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 即nums[mid]>nums[right]的情况，因为各元素不同，因为 nums 是升序序列旋转得到，所以旋转点左右依然有序
                # nums[right] 肯定是某一段的最大值，nums[mid]>nums[right]代表旋转点在mid右侧，也就是说mid左侧现在是有序的
                if nums[left] <= target < nums[mid]:  # 如果target在左侧有序区间
                    right = mid - 1
                else:
                    left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1

          
