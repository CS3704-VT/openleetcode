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


            
    