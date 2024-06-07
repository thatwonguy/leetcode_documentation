<!-- 344. Reverse String
Solved
Easy
Topics
Companies
Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character. -->

class Solution {
    public function reverseString(&$s) {
        $left = 0;
        $right = count($s) - 1;
        
        while ($left < $right) {
            // Swap the elements at left and right pointers
            $temp = $s[$left];
            $s[$left] = $s[$right];
            $s[$right] = $temp;
            
            // Move the pointers
            $left++;
            $right--;
        }
    }
}