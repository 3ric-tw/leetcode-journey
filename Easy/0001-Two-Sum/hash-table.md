# Two Sum: Hash Table Approach

## Problem-Solving Approach

1. Create an empty hash table.
    ```
    {
        # nums_value: nums_index
    }
    ```

2. Iterate through the list, starting from the first element (index 0).
    ```
    nums=[9,8,7,6,5,7]
    for nums_index, nums_value in enumerate(nums):
    ```

    will be like:
    ```
    nums_index: 0, nums_value: 9
    nums_index: 1, nums_value: 8
    nums_index: 2, nums_value: 7
    nums_index: 3, nums_value: 6
    nums_index: 4, nums_value: 5
    nums_index: 5, nums_value: 7
    ```

3. Go through each number in the array

- Calculate the `difference` between the `target` and the current value(`nums_value`).

-  If this `difference` is in our `hash table`, we've found our pair, return the `difference`'s `index` from hash table and `nums_index`.

-  If not, add the `current number(nums_value)` and `its index(nums_index)` to the `hash table`.

## What is the Hash Table
A hash table (dictionary in Python) is like a special notebook:

- Left side: we write the number (key)
- Right side: we write its position in the array (value)
- This allows us to quickly look up if a number exists and find its position.

```
hash_table = {
    # key: value
    9: 0,
    8: 1,
    7: 2,
    6: 3,
    5: 4,
    7: 5
}
```



## Code Example

Here's a Python implementation of the hashtable approach, with added print statements to illustrate the process:

```python
nums=[9,8,7,6,5,7]
target=14
print(f"nums: {nums}\ntarget: {target}")

hash_table={} # nums_value: nums_index
print(f"declare a hash_table: {hash_table}\n-----------")

count=0
for nums_index, nums_value in enumerate(nums):
    count = count+1
    print(f"count: {count}\nnums_index: {nums_index}\nnums_value: {nums_value}\n")

    diff = target - nums_value
    print(f"{diff}={target}-{nums_value}\n")

    print(f"before check diff: {diff} in hash_table, current hash_table: {hash_table}\n")
    if diff in hash_table:
        print(f"Found diff: {diff} in hash_table return Answer: {hash_table[diff]}, {nums_index}\n----------")
    
    else:
        hash_table[nums_value] = nums_index
        print(f"diff: {diff} is not in hash_table, add nums_value: nums_index {nums_value}: {nums_index} in, and current hash_table: {hash_table}\n----------")
```

Output:
```
nums: [9, 8, 7, 6, 5, 7]
target: 14
declare a hash_table: {}
-----------
count: 1
nums_index: 0
nums_value: 9

5=14-9

before check diff: 5 in hash_table, current hash_table: {}

diff: 5 is not in hash_table, add nums_value: nums_index 9: 0 in, and current hash_table: {9: 0}
----------
count: 2
nums_index: 1
nums_value: 8

6=14-8

before check diff: 6 in hash_table, current hash_table: {9: 0}

diff: 6 is not in hash_table, add nums_value: nums_index 8: 1 in, and current hash_table: {9: 0, 8: 1}
----------
count: 3
nums_index: 2
nums_value: 7

7=14-7

before check diff: 7 in hash_table, current hash_table: {9: 0, 8: 1}

diff: 7 is not in hash_table, add nums_value: nums_index 7: 2 in, and current hash_table: {9: 0, 8: 1, 7: 2}
----------
count: 4
nums_index: 3
nums_value: 6

8=14-6

before check diff: 8 in hash_table, current hash_table: {9: 0, 8: 1, 7: 2}

Found diff: 8 in hash_table return Answer: 1, 3
----------
count: 5
nums_index: 4
nums_value: 5

9=14-5

before check diff: 9 in hash_table, current hash_table: {9: 0, 8: 1, 7: 2}

Found diff: 9 in hash_table return Answer: 0, 4
----------
count: 6
nums_index: 5
nums_value: 7

7=14-7

before check diff: 7 in hash_table, current hash_table: {9: 0, 8: 1, 7: 2}

Found diff: 7 in hash_table return Answer: 2, 5
----------
```

## Time Complexity Analysis

- We go through the array once: O(n)
- Hash table lookups are very fast: O(1)
- Overall time complexity: O(n)

This is much faster than the brute force approach, which takes O(n^2) time.

The hash table approach provides an efficient solution to the Two Sum problem. It allows us to find the answer in a single pass through the array, making it much faster than checking every possible pair.