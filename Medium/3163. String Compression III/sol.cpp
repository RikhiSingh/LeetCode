// https://www.youtube.com/watch?v=13NBzSOHZOk

// Time : simply tranmservers the string so O(n)
// Space : O(1) we aint using any extra space

class Solution {
public:
    string compressedString(string word) {
        // n is length of word
        int n = word.length();

        // the answer which we will return in the end
        string ans = "";

        // 3 variables
        // count is the count of consecutive characters
        // i is the index of the current character
        // j is the index of the next character
        int count = 0, i = 0, j = 0;

        // while j is less than n, i.e., we haven't reached the end of the word
        while(j < n){

            // initialize count to 0
            count = 0;

            // while j is less than n 
            // and the current character is equal to the next character
            // and count is less than 9 (the constraint of the problem)
            while(j < n && word[i] == word[j] && count < 9){
                // we move to next character and also add 1 to count
                j++;
                count++;
            }

            // add the count to the answer either when the next character is different or 9 consecutive characters have been encountered
            ans += to_string(count) + word[i];

            // either of the above conditions are true, we move to the next character and set current j as initial that is i
            // set i as current posiition of j
            // which represents the start of the next group of characters to be processed. This means that i is now positioned at the next distinct character, ready to start counting again.
            i = j;
        }

        // return the answer string
        return ans;
    }
};