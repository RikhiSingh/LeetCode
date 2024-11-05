// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful?envType=daily-question&envId=2024-11-05

function minChanges(s: string): number {
    // initial count as we are suppposed to return the minimum number of changes to make the string s beauitiful
    let count = 0;

    // for loop with inital pointer at 0 and final pointer at s.length - 1 (last)
    // and we move by 2 each time because are comparing two numbers already of even lenght substring of 2 characters
    for (let i = 0; i < s.length - 1; i += 2){
        // if the first one and the next one are not equal we increment the count by 1
        if(s[i] !== s[i+1]){
            count++;
        }
    }

    // at the end we return the count
    return count;
};