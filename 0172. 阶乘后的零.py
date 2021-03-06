给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
  
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
  
# 计算因子 5 O(n)
阶乘末尾的每个 0 表示乘以 10, 等于一对 2 和 5 的因子

可以注意到因子 2 数总是比因子 5 大，因此我们可以删除计算因子 2 的过程

考虑到从 1 到 n 的每个数字，只有 5, 10, 15, 20, 25, 30, ... 等等至少有一个因子 5。
所以，我们不必一步一步的往上迭代，可以五步的往上迭代

def trailingZeroes(self, n: int) -> int:     
    zero_count = 0
    for i in range(5, n + 1, 5):
        power_of_5 = 5
        while i % power_of_5 == 0:
            zero_count += 1
            power_of_5 *= 5

    return zero_count
  
# 高效的计算因子 5 O(logn)
我们不必每次尝试 5 的幂，而是每次将 n 本身除以 5

def trailingZeroes(self, n: int) -> int:
    zero_count = 0
    while n > 0:
        n //= 5
        zero_count += n
    return zero_count






  
  
