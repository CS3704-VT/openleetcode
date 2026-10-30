# Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

**Example 2:**
Input: head = [1,2]
Output: [2,1]

**Example 3:**
Input: head = []
Output: []

**Constraints:**

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Note:** The test runner passes the list as an array of values, so `reverseList` takes and returns a list. The solution builds a `ListNode` chain from the input, reverses it, and converts the result back to a list.

## Approach

Build a linked list from the input values. Then walk through it once, keeping a pointer to the previous node. For each node, save its `next`, point it back to the previous node, then move both pointers forward. When the walk finishes, the previous pointer is the new head. Read the values from there into a list and return it.

## Implementation

```python
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: List[int]) -> List[int]:
        dummy = ListNode()
        tail = dummy
        for value in head:
            tail.next = ListNode(value)
            tail = tail.next

        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        result = []
        while prev:
            result.append(prev.val)
            prev = prev.next
        return result
```

## Complexity Analysis

- Time complexity: O(n), since each node is visited a constant number of times.
- Space complexity: O(n) for building the linked list and output list; the reversal itself is done in place with O(1) extra space.