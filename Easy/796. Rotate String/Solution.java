// https://leetcode.com/problems/rotate-string?envType=daily-question&envId=2024-11-03

////=================================================Question Description================================================ 

// 796. Rotate String Easy
// Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

// A shift on s consists of moving the leftmost character of s to the rightmost position.

// For example, if s = "abcde", then it will be "bcdea" after one shift.
 

// Example 1:

// Input: s = "abcde", goal = "cdeab"
// Output: true
// Example 2:

// Input: s = "abcde", goal = "abced"
// Output: false
 

// Constraints:

// 1 <= s.length, goal.length <= 100
// s and goal consist of lowercase English letters.

//// ===============================================Solution Approach================================================
/// 
/// so firstly make sure the length of both string are same 
/// then we add the initial goal to itself
/// for example for abcde will be "abcdeabcde"
/// no matter how many times we shift the string it will be in this concatenated form
/// 
class Solution {
    public boolean rotateString(String s, String goal) {
        return s.length() == goal.length() && (s+s).contains(goal);
    }

    public static void main(String[] args) {
        
        Solution solution = new Solution();
        String s = "abcde";
        String goal = "cdeab";

        boolean result = solution.rotateString(s, goal);
        System.out.println(result); 
    }
}