// BEATS 100% users
// Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

public double findMedianSortedArrays(double A, int[] B) {
    // Merge the two sorted arrays
    int[] mergedArray = mergeTwoSortedArray(A, B);
    int n = mergedArray.length;
    
    // Check if the length of the merged array is odd or even
    // check whether the length of merged array is even or odd
    if (n % 2 == 0) {
        // If even, return the average of the two middle elements
        return (mergedArray[(n - 1) / 2] + mergedArray[n / 2]) / 2.0;
    } else {
        // If odd, return the middle element itself
        return mergedArray[n / 2];
    }
}

public int[] mergeTwoSortedArray(int[] A, int[] B) {
    // start array to store merged array
    int[] merged = new int[A.length + B.length];
    int i = 0, j = 0, k = 0;
    
    // merrge the two sorted arrays until one of them is finished
    while (i < A.length && j < B.length) {
        merged[k++] = (A[i] < B[j]) ? A[i++] : B[j++];
    }
    
    // If remaining elements in array A, append them to the merged array
    while (i < A.length) {
        merged[k++] = A[i++];
    }
    
    // If remaining elements in array B, append them to the merged array
    while (j < B.length) {
        merged[k++] = B[j++];
    }
    
    // Return the merged array
    return merged;
}
