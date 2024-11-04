# https://leetcode.com/problems/circular-sentence?envType=daily-question&envId=2024-11-02

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        # a list of words that is split by space
        w = sentence.split(" ")

        # for each word we get
        for i in range(len(w)):
            # get current word w[i] and its first character [0]
            # if not equal to
            # the previous word is w[i-1] and its last character [-1]
            # then we return False
            if w[i][0] != w[i-1][-1]:
                return False
            # else we return true
            return True
        