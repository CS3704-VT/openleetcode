### Approach

First, confirm the two strings are the same length. Iterate through string s first, then t second. Go through the first string, counting how many times each letter is used in the string by adding one to a 26 index long array (an index for each letter). Then go through the second string, subtracting one from that array for each letter used. If the resulting array is filled with zeros, the two strings are anagrams.

### Implementation

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        nums = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            nums[index] = nums[index] + 1
        for i in range(len(t)):
            index = ord(t[i]) - ord('a')
            nums[index] = nums[index] - 1

        return all(x==0 for x in nums)
```

### Complexity Analysis

* Time complexity: **O(n)**.
* Space complexity: **O(1)**. (fixed length of array every time)