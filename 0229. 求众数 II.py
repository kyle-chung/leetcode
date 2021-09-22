给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

示例 1：

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]

# 摩尔投票
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                if len(dict) < 2:
                    dict[i] = 1
                else:
                    for key in list(dict.keys()):
                        dict[key] -= 1
                        if dict[key] == 0: dict.pop(key)

        res = []
        for key in dict.keys():
            if nums.count(key) > len(nums)/3: res.append(key)
        
        return res

