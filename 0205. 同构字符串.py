给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:

输入：s = "egg", t = "add"
输出：true

示例 2：

输入：s = "foo", t = "bar"
输出：false

本题本质就是找到两个子母中不同字符从左到右的的index 列表是否完全一致

# index
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))

# zip
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s, t)))
      
# haspmap
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1=dict()
        dic2=dict()
        for i in range(len(s)):
            if (s[i] in dic1 and dic1[s[i]]!=t[i]) or (t[i] in dic2 and dic2[t[i]]!=s[i]):
                return False
            dic1[s[i]]=t[i]
            dic2[t[i]]=s[i]
        return True
