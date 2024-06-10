# 387. First Unique Character in a String
# Solved
# Easy
# Topics
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict1 = dict()

        # get a dictionary of the count of all the letters in the word
        for letter in s:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1

        # use the enumerate function to track the index and element of the iterable (dict1 in this case)
        for index, letter in enumerate(s, start=0):
            if dict1[letter] == 1:
                return index
        
        # if all letters repeat return -1
        return -1
            
