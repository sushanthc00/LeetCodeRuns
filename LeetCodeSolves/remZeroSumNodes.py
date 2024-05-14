class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remZeroSumNodes(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        sum = 0

        while current:
            sum += current.val
            if sum == 0:
                if current.next:
                    current.next = current.next.next
                else:
                    break

                if current.next == dummy.next:
                    current = dummy
                else:
                    current = current.next

            else:
                current = current.next

        return dummy.next


def list_to_linked_list(nums):
    """
    Convert a list of integers into a linked list of ListNode objects.
    """
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


if __name__ == '__main__':
    head = list_to_linked_list([1, 2, -3, 3, 1])
    solution = Solution()
    print(solution.remZeroSumNodes(head))
