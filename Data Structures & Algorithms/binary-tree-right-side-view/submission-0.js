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
     * @param {TreeNode} root
     * @return {number[]}
     */
    rightSideView(root) {
        let res = [];
        if (!root) return res;

        let q = [];
        if (root) {
            q.push(root);
        }

        let levelIdx = 0;
        while (q.length) {
           let level = [];

            for (let i = q.length; i > 0; i--) {
                let curr = q.shift();
                if (curr !== null) {
                    level.push(curr.val);
                    q.push(curr.left);
                    q.push(curr.right);
                }
            }

            if (level.length > 0 && level[level.length - 1]) {
                res.push(level[level.length - 1]);
            }
        }

        return res;
    }
}
