/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    // Vector to store the preorder traversal
    vector<int> v;

    // Helper function to perform preorder traversal
    void preOrder(TreeNode* root) {
        if (root == NULL) {
            // Base case: if the node is null, return
            return;
        }
        // Process the current node by adding its value to the vector
        v.push_back(root->val);
        // Recursively traverse the left subtree
        preOrder(root->left);
        // Recursively traverse the right subtree
        preOrder(root->right);
    }

public:
    // Function to return the preorder traversal of the binary tree
    vector<int> preorderTraversal(TreeNode* root) {
        // Perform preorder traversal starting from the root
        preOrder(root);
        // Return the result vector
        return v;
    }
};
