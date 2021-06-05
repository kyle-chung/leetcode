给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 
示例 1：

输入：x = 123
输出：321

示例 2：

输入：x = -123
输出：-321

示例 3：

输入：x = 120
输出：21

要在没有辅助栈或数组的帮助下「弹出」和「推入」数字，我们可以使用如下数学方法：

// 弹出 x 的末尾数字 digit
digit = x % 10
x /= 10

// 将数字 digit 推入 rev 末尾
rev = rev * 10 + digit

注：差不多得了，不喜欢这道题
