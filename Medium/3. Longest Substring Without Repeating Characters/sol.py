# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # fetch the charset 
        charSet = set()

        #  Two pointers for sliding window
        #  Left initialized as zero
        left = 0

        # initalise result
        result = 0

        # r goes from each character
        for right in range(len(s)):
            while s[right] in charSet:

                # remove left most
                charSet.remove(s[left])

                left = left + 1

            # after all duplicates removed add right most one
            charSet.add(s[right])

            result = max(result, right - left + 1)
        return result