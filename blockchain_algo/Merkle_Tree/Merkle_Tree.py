from hashlib import sha256


class MerkleTree:
    def __init__(self, data):
        self.leaves = [sha256(d) for d in data]
        self.root = self.build_merkle_tree(self.leaves)

    def build_merkle_tree(self, leaves):
        if len(leaves) == 1:
            return leaves[0]
        new_leaves = []
        for i in range(0, len(leaves), 2):
            left = leaves[i]
            right = leaves[i + 1] if i + 1 < len(leaves) else leaves[i]
            new_leaves.append(sha256(left + right))
        return self.build_merkle_tree(new_leaves)


data = ["a", "b", "c", "d"]
merkle_tree = MerkleTree(data)
print(f"Merkle Root: {merkle_tree.root}")
