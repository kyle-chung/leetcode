给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807

示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

运行条件：链表从头遍历到位，逐位相加
（1）需要保存进位
（2）需要保存结果
结束时：
（1）两个链表只要有一个非空就需要往后进行
（2）🚩如果链表遍历结束，进位不为0，需要把进位项添加在链表后面

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total%10)
            remainder = total//10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            curr = curr.next

        if remainder : curr.next = ListNode(remainder)
        return result.next
