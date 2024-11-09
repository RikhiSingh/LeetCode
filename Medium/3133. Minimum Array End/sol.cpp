class Solution {
public:
    long long minEnd(int n, int x) {
        // long named result and set it to x as it will be out first element
        long long result = x;
        // loop from 1 to n-1 as we are already setting the first element as x
        for(int i =1; i < n; i++){
            // add 1 to result and OR it with x
            result = (result + 1) | x;
        }
        // return result
        return result;
    }
};