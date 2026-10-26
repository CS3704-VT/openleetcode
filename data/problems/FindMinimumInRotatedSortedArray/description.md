
# Find Minimum in Rotated Sorted Array

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Description

Given a sorted array of unique integers that has been rotated, return the minimum element.

The solution must run in O(log n) time.

## Approach

Use binary search to find the minimum element. Compare the middle element with the rightmost element to determine which half contains the minimum.

## Complexity Analysis

- Time: O(log n)
- Space: O(1)

## Examples

Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0
