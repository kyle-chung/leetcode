给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]

# backtracking
假设我们有 [2, 5, 8, 9, 10] 这 5 个数要填入，已经填到第 3 个位置，已经填了 [8,9] 两个数，那么这个数组目前为 [8, 9 | 2, 5, 10]
分隔符区分了左右两个部分。假设这个位置我们要填 10 这个数，为了维护数组，我们将 2 和 10 交换
即能使得数组继续保持分隔符左边的数已经填过，右边的待填 [8, 9, 10 | 2, 5]

class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res

# dfs
问题：
1、递归函数的内存问题，可以看到每个递归函数切割并且向下传递了一个nums(注意这里切片是产生了一个新数组)
   那么空间复杂度约等于 递归深度 * O(N), 直接大概扩大了n倍
2、每个递归函数里都用了切片： nums[:i]+nums[i+1:]) ，时间复杂度是O(n)(切片的时间复杂度等于切片数组的大小)
   时间复杂度又扩大了n倍。虽然这个方法简单无脑，但是这种做法本质上不够尊重stack这种线性数据结构的特点吧，因为过度切片的问题。

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        elif len(nums) == 2: return [nums,nums[::-1]]

        res = []
        for pos,i in enumerate(nums):
            temp = self.permute(nums[:pos]+nums[pos+1:])
            for item in temp:
                res.append([i]+item)        
        return res

