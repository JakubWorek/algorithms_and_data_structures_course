class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        
        
        
def max_path(root):
    global_max = float('-inf')
    
    def recur(node):
        if not node: return 0
        nonlocal global_max
        
        left_max   = recur(node.left)
        right_max  = recur(node.right)
        global_max = max(global_max, node.val + left_max + right_max)
        curr_max   = max(0, node.val + max(left_max, right_max))
        return curr_max
        
    recur(root)
    
    return global_max

def test():
    v = Node(5)
    u = Node(-2)
    w = Node(3)
    z = Node(10)

    v.left = u
    v.right = w
    w.left = z

    print(max_path(v)) 

    root = Node(-4, 
            Node(10,
                Node(7,
                    Node(8,
                        Node(1,
                            Node(-5,
                                Node(-4)
                            )
                        ),
                        Node(-7, 
                            right=Node(1)
                            )
                    )
                ),
                Node(-5,
                        Node(-100),
                        Node(2,
                            Node(20),
                            Node(7)
                        )
                    )
                ),
            Node(-8)
            )

    print(max_path(root))

test()