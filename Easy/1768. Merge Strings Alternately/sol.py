# https://leetcode.com/problems/merge-strings-alternately?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        
        answer = []
        
        while i < len(word1) and j < len(word2):
            answer.append(word1[i])
            answer.append(word2[j])
            i += 1
            j += 1
        answer += word1[i:]
        answer += word2[j:]
        
    
        return "".join(answer)
        

solution = Solution()
word1 = "a"
word2 = "pqwqag"
print(solution.mergeAlternately(word1, word2)) 