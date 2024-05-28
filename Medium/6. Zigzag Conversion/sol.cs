//  Link: https://leetcode.com/problems/zigzag-conversion/description/

public class Solution {
    // Function to convert the input string into Zigzag pattern based on the given number of rows
    public string Convert(string s, int numRows) {
        // If there's only one row, return the string as is
        if(numRows == 1) return s;

        // Create an array to hold strings for each row
        string [] row = new string[numRows];
        // Initialize each row with an empty string
        for(int i=0; i < numRows; i++){
            row[i]="";
        }

        // Initialize variables to keep track of current row and direction of traversal
        var curRow = 0; // Current row index
        var goingDown = false; // Flag to indicate whether moving downwards or upwards

        // Iterate through each character in the input string
        foreach(char c in s){
            // Append the current character to the string of the current row
            row[curRow] += c;

            // Check if it's time to change direction
            if(curRow == 0 || curRow == numRows - 1){
                goingDown = !goingDown; // Toggle the direction
            }

            // Update the current row index based on the direction
            if(goingDown){
                curRow++; // Move downwards
            }
            else{
                curRow--; // Move upwards
            }
        }

        // Concatenate the strings from each row to form the final result
        string result = "";
        for(int i=0; i < row.Length; i++){
            result += row[i];
        }
        // Return the Zigzag pattern as a single string
        return result;
    }
}
