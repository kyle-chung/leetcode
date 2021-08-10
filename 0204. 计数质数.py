统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 枚举
def countPrimes(n):
    is_prime = [True]*(n)
    ans = 0
    for num in range(2,n): 
        if is_prime[num]:
            ans+=1
            # 右边界:因为数字最大是n-1 所以只需要到(n-1)//num 右边是开区间 所以+1
            for k in range(1,(n-1)//num+1):
                is_prime[num*k]=False
    return ans


