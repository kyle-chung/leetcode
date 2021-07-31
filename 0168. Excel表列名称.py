给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"

# O(log 26 * columnNumber)
这是一道从 1 开始的的 26 进制转换题。

对于一般性的进制转换题目，只需要不断地对 columnNumber 进行 % 运算取得最后一位
然后对 columnNumber 进行 // 运算，将已经取得的位数去掉，直到 columnNumber 为 0 即可。

但本题需要我们将从 1 开始，因此在执行「进制转换」操作前，我们需要先对 columnNumber 执行减一操作，从而实现整体偏移

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(ans[::-1])
    
ord() 函数是 chr() 函数（对于8位的ASCII字符串）的配对函数
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值


