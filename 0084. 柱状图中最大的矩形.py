给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:

输入: [2,1,5,6,2,3]
输出: 10
  
我们需要在柱状图中找出最大的矩形
如果我们枚举「高」，我们可以使用一重循环枚举某一根柱子，将其固定为矩形的高度 h
随后我们从这跟柱子开始向两侧延伸，直到遇到高度小于 h 的柱子，就确定了矩形的左右边界
如果左右边界之间的宽度为 w，那么对应的面积为 w * h

# 单调栈 时间复杂度：O(N)
我们可以对数组从左向右进行遍历，同时维护一个「可能作为答案」的数据结构，其中按照从小到大的顺序存放了一些 j（高度） 值

用相同的方法，我们从右向左进行遍历
在得到了左右两侧的柱子之后，我们就可以计算出每根柱子对应的左右边界，并求出答案了

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
      
我们用一个具体的例子 [6, 7, 5, 2, 4, 5, 9, 3] 来帮助读者理解单调栈。
我们需要求出每一根柱子的左侧且最近的小于其高度的柱子。初始时的栈为空。

这里会有一种特殊情况。如果我们移除了栈中所有的 j 值，那就说明 i 左侧所有柱子的高度都大于 height[i]
那么我们可以认为 i 左侧且最近的小于其高度的柱子在位置 j = -1
它是一根「虚拟」的、高度无限低的柱子。这样的定义不会对我们的答案产生任何的影响
我们也称这根「虚拟」的柱子为「哨兵」

我们枚举 6，因为栈为空，所以 6 左侧的柱子是「哨兵」，位置为 -1。随后我们将 6 入栈。

栈：[6(0)]。（这里括号内的数字表示柱子在原数组中的位置）
我们枚举 7，由于 6 < 7，因此不会移除栈顶元素，所以 7 左侧的柱子是 6，位置为 0。随后我们将 7 入栈。

栈：[6(0), 7(1)]
我们枚举 5，由于 7 > 5，因此移除栈顶元素 7。同样地，6 > 5，再移除栈顶元素 6。此时栈为空
所以 5 左侧的柱子是「哨兵」，位置为 -1。随后我们将 5 入栈。

栈：[5(2)]
接下来的枚举过程也大同小异。我们枚举 2，移除栈顶元素 5，得到 2 左侧的柱子是「哨兵」，位置为 -1。将 2 入栈。

栈：[2(3)]
我们枚举 4，5 和 9，都不会移除任何栈顶元素，得到它们左侧的柱子分别是 2，4 和 5，位置分别为 3，4 和 5。将它们入栈。

栈：[2(3), 4(4), 5(5), 9(6)]
我们枚举 3，依次移除栈顶元素 9，5 和 4，得到 3 左侧的柱子是 2，位置为 3。将 3 入栈。

栈：[2(3), 3(7)]

# 单调栈 + 常数优化 时间复杂度：O(N)
在方法一中，我们在对位置 i 进行入栈操作时，确定了它的左边界
从直觉上来说，与之对应的我们在对位置 i 进行出栈操作时可以确定它的右边界

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans



      
      
      
      
      
