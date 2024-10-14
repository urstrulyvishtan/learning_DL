# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        def serialize_helper(node):
            if not node:
                return "null,"  # Use 'null' to represent null nodes
            return str(node.val) + "," + serialize_helper(node.left) + serialize_helper(node.right)

        return serialize_helper(root)

    def deserialize(self, data: str) -> TreeNode:
        def deserialize_helper(values):
            value = next(values)  # Get the next value from the iterator
            if value == "null":
                return None  # If the value is 'null', return None
            node = TreeNode(int(value))  # Create a new TreeNode
            node.left = deserialize_helper(values)  # Recursively build the left subtree
            node.right = deserialize_helper(values)  # Recursively build the right subtree
            return node

        values = iter(data.split(","))  # Split the string and create an iterator
        return deserialize_helper(values)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))