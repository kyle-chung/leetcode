给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：

输入：s = "0000"
输出：["0.0.0.0"]

# backtrack
class Solution(object):
    def restoreIpAddresses(self, s):
        self.res = []

        def backtrack(s, tmp):
            if len(s) == 0 and len(tmp) == 4:
                self.res.append('.'.join(tmp))
                return
            if len(tmp) < 4:
                for i in range(min(3, len(s))):
                    p, n = s[:i + 1], s[i + 1:]
                    if p and 0 <= int(p) <= 255 and str(int(p)) == p:
                        backtrack(n, tmp + [p])

        backtrack(s, [])
        return self.res
