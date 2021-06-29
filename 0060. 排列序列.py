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

def getPermutation(n: int, k: int) -> str:
    factorial = [1]  # n 阶乘 映射集 0...n-1
    for i in range(1, n):
        factorial.append(factorial[-1] * i)

    k -= 1
    '''
    k 需要先自减一 原因：
    不妨设分子为 k，那么得到的公式可能是这样的：
        ai =  ⌊k / (n-1)!⌋ + 1
    尝试使用以上公式计算 a1:
        （1）当 k < (n-1)! 时，a1 = ⌊k / (n-1)!⌋ + 1 = 1，正确
        （2）当 k = (n-1)! 时，a1 = ⌊k / (n-1)!⌋ + 1 = 2，错误
    而使用 ai =  ⌊(k-1) / (n-1)!⌋ + 1 却能正确处理这种情况
    即：只是简洁了数学公式的使用，如果不自减一的话，需要应对多种情况
    '''
    ans = list()  # 结果集
    valid = [1] * (n + 1)  # 0，1...n 排列标志集，标识在一整次寻找中哪个数已进排列中
    for i in range(1, n + 1):  # 排列中 依次取得的排列的数的个数 1个...n个
        order = k // factorial[n - i] + 1  # 此公式可算出上面的数对应的从 1...n 中哪个数 order  | n - i 为了对应 factorial 下标,获取剩余个数排列种类总数
        for j in range(1, n + 1):  # 依次寻找对应的数 从 1...n
            order -= valid[j]  # 找到一个数，若没有进入过结果排列集，减一，直至 order == 0 则表示找到该排列中的第 i 个数，修改标志集对应位置为已进入结果排序集
            if order == 0:
                ans.append(str(j))
                valid[j] = 0
                break
        k %= factorial[n - i]  # 之后 k 对于已取得的数的排列位数取余，得到下一位需要的

    return "".join(ans)








