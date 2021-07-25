给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

# dp 时间复杂度：O(n^2)
初始化 dp = [False,⋯,False]，长度为 n+1。
n 为字符串长度。dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。

初始化 dp[0]=True，空字符可以被表示

若 dp[i]=True 且 s[i,⋯,j] 在 wordlist 中：dp[j]=True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:       
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]


