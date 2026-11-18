# Container With Most Water — Python Solution

## Approach

Use two pointers, one at the beginning of the array and one at the end.

Calculate the area between the two lines using the shorter height multiplied by the distance between them.

Keep track of the largest area found. Move the pointer at the shorter line inward because moving the taller line cannot produce a larger area with the same shorter height.

Continue until the pointers meet.

## Complexity

- **Time:** O(n), because each pointer moves inward at most n times.
- **Space:** O(1), because only a few variables are used.