给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

示例 1：

输入：n = 3, k = 3
输出："213"

示例 2：

输入：n = 4, k = 9
输出："2314"


# 数学 + 缩小问题规模 时间复杂度：O(n^2)
思路
要想解决本题，首先需要了解一个简单的结论：

对于 n 个不同的元素（例如数 1, 2,⋯,n），它们可以组成的排列总数目为 n!

我们首先确定排列中的首个元素 a1。根据上述的结论，我们可以知道：

以 1 为 a1 的排列一共有 (n-1)! 个；
以 2 为 a1 的排列一共有 (n-1)! 个；
以 n 为 a1 的排列一共有 (n-1)! 个

这样一来，我们就把原问题转化成了一个完全相同但规模减少 1 的子问题

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)









