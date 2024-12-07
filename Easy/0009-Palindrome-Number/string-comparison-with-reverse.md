# Palindrome Number: String Comparison with Reverse Approach

## Problem-Solving Approach

To determine if a number is a palindrome, we can convert it to a string and compare it with its reverse. 
Here's a step-by-step breakdown of the approach:

1. Convert the input integer to a string.
2. Create a reversed version of the string using Python's slicing feature.
3. Compare the original string with its reverse.
4. If they are the same, the number is a palindrome; otherwise, it's not.

This approach leverages Python's string slicing capability, particularly the `::-1` syntax, which creates a reversed copy of the string.

## Understanding Python Slicing

The basic syntax for slicing is:

```
sequence[start:end:step]
```

- `start`: The beginning index of the slice (inclusive)
- `end`: The ending index of the slice (exclusive)
- `step`: The increment between each item in the slice

If you omit these parameters, Python uses default values:
- `start` defaults to the beginning of the sequence
- `end` defaults to the end of the sequence
- `step` defaults to 1

Here are some basic examples to illustrate how slicing works:

```python
# Example: Basic slicing
text = "Hello, World!"
print(text[0:5])   # Output: Hello
print(text[7:12])  # Output: World

# Example: Using step
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])  # Output: [0, 2, 4, 6, 8]
print(numbers[1::2]) # Output: [1, 3, 5, 7, 9]
```

### The ::-1 Syntax

The `::-1` syntax is a special case of slicing:

```python
sequence[::-1]
```

This means:
- Start from the end (because `start` is omitted)
- Go to the beginning (because `end` is omitted)
- Move with a step of -1 (i.e., go backwards)

This effectively reverses the sequence, which is perfect for our palindrome check. Here are some examples:

```python
# Example: Reversing sequences
text = "Hello, World!"
print(text[::-1])  # Output: !dlroW ,olleH

numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1]

# Example: Reversing part of a sequence
print(text[5::-1])  # Output: ,olleH
```

### Supported Data Types

Python slicing works with several sequence types:

- String
- List
- Tuple
- Range
- Bytes
- Bytearray

## Code Example

Here's a Python implementation of the string comparison with reverse approach:

```python
def isPalindrome(x):
    print(f"input: {x}")

    # Convert int to string
    str_x = str(x)

    print(f"str_x: {str_x}\nreversed_str_x: {str_x[::-1]}")

    # Compare the string with its reverse
    return str_x == str_x[::-1]

# Test cases
test_cases = [0, 5, 10, 11, 121, 1221, -5, -10, -11, -121, -1221]
for test_case_input in test_cases:
    print(f"isPalindrome: {isPalindrome(test_case_input)}\n-------")
```

Output:
```
input: 0
str_x: 0
reversed_str_x: 0
isPalindrome: True
-------
input: 5
str_x: 5
reversed_str_x: 5
isPalindrome: True
-------
input: 10
str_x: 10
reversed_str_x: 01
isPalindrome: False
-------
input: 11
str_x: 11
reversed_str_x: 11
isPalindrome: True
-------
input: 121
str_x: 121
reversed_str_x: 121
isPalindrome: True
-------
input: 1221
str_x: 1221
reversed_str_x: 1221
isPalindrome: True
-------
input: -5
str_x: -5
reversed_str_x: 5-
isPalindrome: False
-------
input: -10
str_x: -10
reversed_str_x: 01-
isPalindrome: False
-------
input: -11
str_x: -11
reversed_str_x: 11-
isPalindrome: False
-------
input: -121
str_x: -121
reversed_str_x: 121-
isPalindrome: False
-------
input: -1221
str_x: -1221
reversed_str_x: 1221-
isPalindrome: False
-------
```

## Time Complexity Analysis

The `time complexity` of this approach is `O(n)`, where n is the number of digits in the input number. This is because:

1. Converting the integer to a string takes O(n) time.
2. Creating the reversed string using slicing takes O(n) time.
3. Comparing the two strings takes O(n) time in the worst case.

The `space complexity` is also `O(n)` as we create two string copies of the number (the original and the reversed version).

This approach is efficient for most practical purposes and takes advantage of Python's built-in string manipulation capabilities. However, it does use extra space to store the string representations, which might be a consideration for very large numbers or memory-constrained environments.
