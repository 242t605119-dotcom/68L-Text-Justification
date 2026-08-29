# LeetCode 68 – Text Justification

Given an array of words and an integer `maxWidth`, format the text so that each line has exactly `maxWidth` characters.

Words should be packed into each line as much as possible.

Except for the last line, spaces should be distributed evenly between the words.

## Example

### Input

```text
words = ["This","is","an","example","of","text","justification."]
maxWidth = 16
```

### Output

```text
[
    "This    is    an",
    "example  of text",
    "justification.  "
]
```

## Approach

I process the words one by one and build each line.

For every line:

1. Add as many words as can fit within `maxWidth`.
2. Calculate the remaining spaces.
3. Distribute the spaces evenly between the words.
4. For the last line, keep only one space between words and add the remaining spaces at the end.
5. Continue until all words are processed.

## Complexity

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(N)`

## Language

**Python**

## LeetCode

**Problem:** 68. Text Justification
**Difficulty:** Hard
**Topic:** Array, String, Simulation

## Author

T.Nandhini
