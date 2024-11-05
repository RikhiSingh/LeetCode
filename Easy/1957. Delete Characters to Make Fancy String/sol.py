# https://leetcode.com/problems/delete-characters-to-make-fancy-string?envType=daily-question&envId=2024-11-01

class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize the stack
        stack = []

        # Iterate over each character through the string
        for c in s:
            # We add current character to the stack
            stack.append(c)

            # If stack has more than 3 characters and and last three are same
            if len(stack) >=3 and (stack[-1] == stack[-2] == stack[-3]):
                # Remove the most recent character (preventing three consecutive same characters)
                stack.pop()
                
        # Join the stack to get the final string
        return "".join(stack)