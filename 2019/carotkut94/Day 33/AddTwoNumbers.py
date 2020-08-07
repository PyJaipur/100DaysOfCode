"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Author : Sidhant Rajora

Problem statement can be found at : https://leetcode.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        start = l1
        carry = (l1.val+l2.val)//10
        l1.val = (l1.val+l2.val)%10
        while l1.next != None and l2.next!=None:
            carry += l1.next.val
            carry += l2.next.val
            l1.next.val = carry % 10
            carry = carry // 10
            l1 = l1.next
            l2 = l2.next
        if l1.next == None:
            l1.next = l2.next
        while l1.next != None:
            carry += l1.next.val
            l1.next.val = carry % 10
            carry = carry // 10
            l1 = l1.next
        if carry>0:
            l1.next = ListNode(carry)
        return start