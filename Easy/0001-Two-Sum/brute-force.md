# Two Sum: Brute Force Approach

## Problem-Solving Approach

The most intuitive solution to the Two Sum problem involves iterating through the list of numbers and checking all possible pairs. Here's a step-by-step breakdown of the brute force approach:

1. Iterate through the list, starting from the first element (index 0).
2. For each element, iterate through the remaining elements in the list.
3. Check if the sum of the current pair equals the target sum.
4. If a match is found, return the indices of the two numbers.
5. If no match is found after checking all pairs, return an appropriate indication (e.g., an empty list or null).

Let's consider a list with four elements as an example:

- First iteration (i=0):
  - Check sum of list[0] + list[1]
  - Check sum of list[0] + list[2]
  - Check sum of list[0] + list[3]

- Second iteration (i=1):
  - Check sum of list[1] + list[2]
  - Check sum of list[1] + list[3]

- Third iteration (i=2):
  - Check sum of list[2] + list[3]

- Fourth iteration (i=3):
  - No elements left to sum with list[3]

This process continues until we find a pair that sums to the target or until we've exhausted all possible pairs.

## Code Example

Here's a Python implementation of the brute force approach, with added print statements to illustrate the process:

```python
nums = [3,2,1,0]
target = 3

print(f"nums: {nums}\ntarget: {target}")
print(f"len_nums: {len(nums)}\nrange: {range(len(nums))}")

for i in range(len(nums)):
    print(f"i: {i}")

    for j in range(i+1, len(nums)):
        print(f"nums[{i}]: {nums[i]}\nnums[{j}]: {nums[j]}\n------------\n")
            
        if nums[i] + nums[j] == target:
            print(f"Answer: i:{i}, j:{j}\n------------\n")
```

Output:
```
nums: [3, 2, 1, 0]
target: 3
len_nums: 4
range: range(0, 4)
i: 0
nums[0]: 3
nums[1]: 2
------------

nums[0]: 3
nums[2]: 1
------------

nums[0]: 3
nums[3]: 0
------------

Answer: i:0, j:3
------------

i: 1
nums[1]: 2
nums[2]: 1
------------

Answer: i:1, j:2
------------

nums[1]: 2
nums[3]: 0
------------

i: 2
nums[2]: 1
nums[3]: 0
------------

i: 3
```

## Time Complexity Analysis

The time complexity of this brute force approach is `O(n²)`, where n is the number of elements in the input list. This is because:

- The outer loop runs n times.
- For each iteration of the outer loop, the inner loop runs (n-1), (n-2), ..., 1 times.
- This results in approximately n * (n-1) / 2 operations, which simplifies to O(n²).

While this approach is straightforward and works for small inputs, it becomes inefficient for larger lists due to its quadratic time complexity.
