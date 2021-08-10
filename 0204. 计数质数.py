统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 埃氏筛
class Solution:
    def countPrimes(self, n: int) -> int:
        # 定义数组标记是否是质数
        is_prime = [1] * n
        
        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                # reason：假设 y < i*i，且 y/i = x(显然 x<i),则 is_prime[j]在 j == x 时已标记为0
                for j in range(i*i, n, i):
                    is_prime[j] = 0

        return count

线性筛

此方法不属于面试范围范畴，本节只做简单讲解。

埃氏筛其实还是存在冗余的标记操作，比如对于 45 这个数，它会同时被 3,,5 两个数标记为非质数
因此我们优化的目标是让每个合数只被标记一次，这样时间复杂度即能保证为 O(n)
