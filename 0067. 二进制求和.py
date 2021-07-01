给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"

# 模拟
先将 a 和 b 转化成十进制数，求和后再转化为二进制数
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = str(int(a)+int(b))
        res = list(res)
        
        for i in range(-1,-len(res)-1,-1):
            if int(res[i])//2 == 0:
                continue
            else:
                res[i] = str(int(res[i])%2)
                try:
                    res[i-1] = str(int(res[i-1])+1)
                except:
                    res = ['1']+res
                    return ''.join(res)

        return ''.join(res)
  
# 位运算
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, base=2), int(b, base=2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

