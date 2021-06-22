给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# backtracking
解决重复问题，我们只要设定一个规则，保证在填第 idx 个数的时候重复数字只会被填入一次即可。
而在本题解中，我们选择对原数组排序，保证相同的数字都相邻
然后每次填入的数一定是这个数所在重复数集合中「从左往右第一个未被填过的数字」

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        ans=[]
        n=len(nums)
        visited=[0]*n
        def dfs():
            if len(ans)==n:
                res.append(ans[::])
            for i in range(n):
                if visited[i] or i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                ans.append(nums[i])
                visited[i]=1
                dfs()
                ans.pop()
                visited[i]=0
        dfs()
        return res

# dfs
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]

        res = []
        for pos,i in enumerate(nums):
            temp = self.permuteUnique(nums[:pos]+nums[pos+1:])
            for item in temp:
                if [i]+item not in res:
                    res.append([i]+item)        
        return res
      
      
      
      
      
      
