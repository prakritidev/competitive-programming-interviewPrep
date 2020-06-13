class InvertBinaryTree {
	class Node {
		int val;
		Node left, right;

		Node(int data) {
			this.val = data;
			left = right = null;
		}

		public void showData() {
			System.out.println(val + " ");
		}
	}

	private Node root;

	InvertBinaryTree() {
		root = null;
	}

	// example got polymorphism (same function name but different params)
	public void insert(int data) {
		root = insert(root, data);
	}

	public Node insert(Node node, int data) {
		if (node == null) {
			return new Node(data);
		} else if (data < node.val) {
			node.left = insert(node.left, data);
		} else if (data > node.val) {
			node.right = insert(node.right, data);
		}
		return node;
	};

	// Inorder printing
	public void inorder(Node root) {
		if (root != null) {
			inorder(root.left);
			System.out.println(root.val);
			inorder(root.right);
		}
	};

	// Invert Tree
	public Node invert(Node node) {
		if (node == null) {
			return null;
		}
		Node temp = invert(root.left);
		node.right = invert(root.right);
		node.left = temp;

		return node;
	}

	// Tree vis

	public static void main(String[] args) {
		// creating object of a class
		InvertBinaryTree tree = new InvertBinaryTree();
		// we can also insert using command line Scanner class.
		tree.insert(50);
		tree.insert(50);
		tree.insert(70);
		tree.insert(15);
		tree.insert(35);
		tree.insert(30);
		tree.insert(31);
		System.out.println("Inorder traversal of binary tree");
		tree.inorder(tree.root);

	}
}