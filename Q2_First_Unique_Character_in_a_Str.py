"""Q2) First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters."""

Solution:

def firstUniqChar(s):
    """
    Finds the index of the first non-repeating character in a given string.
    Returns -1 if no unique character exists.
    """
    # Count the frequency of each character using a dictionary
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the index of the first non-repeating character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    return -1
s1=input() #enter the string
print(firstUniqChar(s1))
