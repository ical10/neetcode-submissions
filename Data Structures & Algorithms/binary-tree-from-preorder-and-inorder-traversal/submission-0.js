/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        // define global vars
        let preIdx = 0;

        // convert inorder array into a hashmap for O(1) find
        let indices = new Map();
        inorder.forEach((val, i) => indices.set(val, i));

        // perform DFS to reconstruct the tree
        function dfs(l, r) {
            if (l > r) return null;
            let root_val = preorder[preIdx++];
            let tree = new TreeNode(root_val);
            let mid = indices.get(root_val);
            tree.left = dfs(l, mid - 1);
            tree.right = dfs(mid + 1, r);
            return tree; 
        }

        return dfs(0, inorder.length - 1);
    }
}
