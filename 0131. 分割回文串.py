给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

# 回溯 + 动态规划预处理 时间复杂度：O(n⋅2^n)
当我们在判断 s[i..j] 是否为回文串时，常规的方法是使用双指针分别指向 i 和 j
每次判断两个指针指向的字符是否相同，直到两个指针相遇
然而这种方法会产生重复计算

设 f(i,j) 表示 s[i..j] 是否为回文串，那么有状态转移方程：
f(i,j) = f(i+1, j-1) and s[i] == s[j]

预处理完成之后，我们只需要 O(1)O(1) 的时间就可以判断任意 s[i..j] 是否为回文串了

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret

# 回溯 + 记忆化搜索 复杂度同上
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret











