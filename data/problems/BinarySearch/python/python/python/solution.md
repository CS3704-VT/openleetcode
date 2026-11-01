### Approach

Because nums is sorted, we can repeatedly cut the search range in half.
Compare target to the middle element: if they match, return the index; if
the middle is smaller, the target must be to the right; otherwise it must
be to the left.

### Implementation

Keep two pointers, left and right, around the part of the array that could
still contain the target. Each loop checks the middle index and moves one
pointer past it. If left passes right, the target is not in the array, so
return -1.

### Complexity Analysis

* Time complexity: O(log n), since the search range halves each step.
* Space complexity: O(1), only a few index variables are used.
