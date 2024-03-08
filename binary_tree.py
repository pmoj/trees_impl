from typing import Optional

class Node:

    def __init__(
        self, 
        val: int, 
        right: Optional["Node"], 
        left: Optional["Node"], 
        prev: Optional["Node"]
    ):
        self.val = val
        self.right = right
        self.left = left
        self.prev = prev

""" 
BINARY TREE
"""

def rotate_right(node: Node) -> Node:

    curr = node
    if curr.left is not None:
        curr.left.right, curr.left.prev, curr.left = curr, curr.prev, curr.left.right
    return curr

def rotate_left(node: Node) -> Node:

    curr = node
    if curr.right is not None:
        curr.right.left, curr.right.prev, curr.right = curr, curr.prev, curr.right.left
    return curr


def add_to_tree(root: Node, node: Node) -> Node:

    curr = root
    while(curr is not None):
        if(node.val == curr.val):
            raise Exception("Node already exists in the tree.")
        if(node.val > curr.val):
            if curr.right is None:
                curr.rigt = node
                node.prev = curr
                return root
            curr = curr.right
        else:
            if curr.left is None:
                curr.left = node
                node.prev = curr
                return root
            curr = curr.left

def remove_from_tree(root: Node, value: int) -> Node | None:

    curr = root
    last = None
    while(curr is not None):
        # root is value
        if(curr.val == value and last == None):
            
        if(curr.val >= value):
            if curr.right is not None:
                curr.prev.right, curr.right = 
            


def find_nth_largest(n: int, root: Node) -> Node | None:
    # find big guy
    if n < 1:
        return None
    curr = root.right
    count = 0
    while(curr is not None):
        if curr.right is not None:
            curr = curr.right
        else:
            break
    last = curr
    while count < n:
        if curr is None:
            raise Exception(
                "Could not find the nth largest, the tree was too "+ \
            "short."
            )
        elif last == curr.right:
            count += 1
            if curr.left:
                curr, last = curr.left, curr
                continue
            curr, last = curr.prev, curr
            continue
        elif last == curr.left:
            if curr.prev is None:
                raise Exception(
                    "Could not find the nth largest, the tree was "+ \
                        "too short."
                )
            curr, last = curr.prev, curr
        elif last == curr.prev:
            if curr.right:
                curr, last = curr.right, curr
                continue
            if curr.left:
                curr, last = curr.left, curr
                continue
            count += 1
            curr, last = curr.prev, curr
            continue
        else:
            count += 1
            curr, last = curr.prev, curr

    return last

if __name__ == "__main__":
        
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)

    n1.prev = n2
    n2.left = n1
    n2.right = n3
    n2.prev = n4
    n3.prev = n2
    n4.left = n2
    n4.right = n6
    n4.prev = n8
    n6.prev = n4
    n6.left = n5
    n6.right = n7
    n5.prev = n6
    n7.prev = n6
    n8.left = n4
    n8.right = n10
    n10.prev = n8
    n10.left = n9
    n10.right = n12
    n9.prev = n10
    n12.prev = n10
    n12.left = n11
    n12.right = n13
    n11.prev = n12
    n13.prev = n12

    n = find_nth_largest(5, n8)
    if n is None:

