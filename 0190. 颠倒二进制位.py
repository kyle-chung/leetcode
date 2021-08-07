颠倒给定的 32 位无符号整数的二进制位。

示例 1：

输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
     因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。

# 逐位颠倒 时间复杂度：O(1)
每次把 res 左移，把 n 的二进制末尾数字，拼接到结果 res 的末尾。然后把 n 右移
从而获得 n 的倒序 res

class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

# 分而治之
若要翻转一个二进制串，可以将其均分成左右两部分，对每部分递归执行翻转操作，然后将左半部分拼在右半部分的后面，即完成了翻转
类似于归并排序

class Solution:
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;

32位无符号整数，如 1111 1111 1111 1111 1111 1111 1111 1111 
表示成16进制        f    f    f    f    f    f    f   f
一个16进制的f代表二进制的4位
ffff ffff右移16位，变成 0000 ffff
ffff ffff左移16位，变成 ffff 0000
它们俩相或，就可以完成低16位与高16位的交换

之后的每次分治，都要先与上一个掩码，再进行交换
      
      
      
