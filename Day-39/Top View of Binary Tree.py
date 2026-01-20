// Node Structure
class Node {
    constructor(val) {
        this.data = val;
        this.left = null;
        this.right = null;
    }
}

function topView(root) {

    // base case
    if (root === null) return [];
    let temp = null;

    // creating empty queue for level order traversal.
    const q = [];

    // creating a map to store nodes at a
    // particular horizontal distance.
    const mp = {};

    let mn = Infinity;
    q.push([root, 0]);

    while (q.length > 0) {
        let [temp, d] = q.shift(); // destructure Node and hd correctly
        mn = Math.min(mn, d);

        // storing temp.data in map.
        if (!(d in mp)) {
            mp[d] = temp.data;
        }

        // if left child of temp exists, pushing it in
        // the queue with the horizontal distance.
        if (temp.left) {
            q.push([temp.left, d - 1]);
        }

        // if right child of temp exists, pushing it in
        // the queue with the horizontal distance.
        if (temp.right) {
            q.push([temp.right, d + 1]);
        }
    }

    const ans = new Array(Object.keys(mp).length);

    // traversing the map and storing the nodes in list
    // at every horizontal distance.
    for (const key in mp) {
        ans[key - mn] = mp[key];
    }

    return ans;
}

// Driver Code
  
    // Create a sample binary tree
        //     10
        //    / \
        //   20  30
        //  / \   / \
        // 40  60 90  100
const root = new Node(10);
root.left = new Node(20);
root.right = new Node(30);
root.left.left = new Node(40);
root.left.right = new Node(60);
root.right.left = new Node(90);
root.right.right = new Node(100);

const result = topView(root);
console.log(result.join(" "));
