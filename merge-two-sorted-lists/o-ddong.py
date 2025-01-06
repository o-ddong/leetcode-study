"""
TC - O(n)
    ㄴ 주어진 두 개의 연결 리스트를 순차적으로 탐색하며 끝까지 확인하는 문제입니다.
    ㄴ 따라서, 노드의 수만큼 반복되니 O(list1 + list2) = O(n)이라고 생각합니다.
SC - O(1)
    ㄴ 포인터(current)를 제외한 나머지는 기존에 존재하는 리스트이므로 O(1)이라고 생각합니다.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next