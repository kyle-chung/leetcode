给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
 
示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

class Solution:
    def summaryRanges(self, nums):
#       Sentinel Node
        nums.append(2 ** 32)
        ret, start = [], 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if i - 1 == start:
                    ret.append(str(nums[start]))
                else:
                    ret.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        return ret
      
这种题和单调栈有一个共同的思路就是添加哨兵节点
我们在nums的末尾append一个2 ** 32，保证最后一次将所有区域全部计算，可以减少循环后的再次判断场景


