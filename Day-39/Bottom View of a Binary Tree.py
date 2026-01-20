// Node Structure
class Node {
    constructor(x) {
        this.data = x;
        this.left = null;
        this.right = null;
    }
}

function bottomView(root) {

    if (root === null) return [];

    // HashMap to store
    // <vertical_index, node data>
    let hash = new Map();

    let minHD = 0;
    let maxHD = 0;

    // Queue for level order traversal 
    // with pair<Node, vertical index>
    let q = [];

    q.push([root, 0]);

    while (q.length > 0) {
        let top = q.shift();

        let node = top[0];
        let hd = top[1];

        // Update the horizontal distance -> node data
        hash.set(hd, node.data);

        minHD = Math.min(minHD, hd);
        maxHD = Math.max(maxHD, hd);

        if (node.left !== null) {
            q.push([node.left, hd - 1]);
        }

        if (node.right !== null) {
            q.push([node.right, hd + 1]);
        }
    }

    let ans = [];
    for (let i = minHD; i <= maxHD; i++) {
        ans.push(hash.get(i));
    }

    return ans;
}

// Driver code

// Create binary tree
//       20
//      /  \
//    8     22
//   / \     \
//  5   3     25
//     / \    /
//    10 14  28

let root = new Node(20);
root.left = new Node(8);
root.right = new Node(22);
root.left.left = new Node(5);
root.left.right = new Node(3);
root.right.left = new Node(4);
root.left.right.left = new Node(10);
root.left.right.right = new Node(14);
root.right.right = new Node(25);
root.right.right.left = new Node(28);

let result = bottomView(root);
console.log(...result);
