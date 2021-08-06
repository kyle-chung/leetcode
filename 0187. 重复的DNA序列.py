所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

示例 1：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]

示例 2：

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]


这个问题的衍生问题是解决任意长度 L 的相同问题
我们将讨论三种不同的方法，它们都是基于滑动窗口和 hashset 的，关键是如何实现一个窗口切片

在线性时间 O(L) 内获取窗口切片很简单也比较笨。
总的来说，这样回导致 O((N−L)L) 的时间消耗和巨大的空间消耗

常数时间的窗口切片 O(1) 是一个好的方法，根据实现方式可以分为两种方法：

Rabin-Karp 算法 = 使用旋转哈希算法实现常数窗口切片。
位操作 = 使用掩码实现常数窗口切片。


# 线性时间窗口切片 + HashSet
时间复杂度：O((N−L)L)
空间复杂度：O((N−L)L) 去存储 HashSet，由于 L=10 最终为时间复杂度为 O(N)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)     
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output

