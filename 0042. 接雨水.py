给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水 

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

# 暴力
暴力的做法是对于数组 height 中的每个元素，分别向左和向右扫描并记录左边和右边的最大高度，然后计算每个下标位置能接的雨水量。
左扫描和右扫描中重复的接水即为实际的接水量
假设数组 height 的长度为 n，该做法需要对每个下标位置使用 O(n) 的时间向两边扫描并得到最大高度，因此总时间复杂度是 O(n^2)

# dp 时间复杂度：O(n)
暴力法的时间复杂度较高是因为需要对每个下标位置都向两边扫描。
如果已经知道每个位置两边的最大高度，则可以在 O(n) 的时间内得到能接的雨水总量。
使用动态规划的方法，可以在 O(n) 的时间内预处理得到每个位置两边的最大高度。

创建两个长度为 n 的数组 leftMax 和 rightMax。对于 0 ≤ i < n, leftMax[i] 表示下标 i 及其左边的位置中，height 的最大高度
rightMax[i] 表示下标 i 及其右边的位置中，height 的最大高度

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

      
      
      
      
