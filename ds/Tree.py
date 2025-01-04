class Node():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = Node()

    def is_empty(self):
        return (self.root.val == None)
    
    def insert(self, val):
        if(self.is_empty()):
            self.root = Node(val)
            return
        else:
            cur_node = self.root
            while cur_node != None:
                if(val <= cur_node.val):
                    if(cur_node.left != None): 
                        cur_node = cur_node.left
                    else: 
                        cur_node.left = Node(val)
                        return
                else:
                    if(cur_node.right != None): 
                        cur_node = cur_node.right
                    else: 
                        cur_node.right = Node(val)
                        return

    def search(self, val):
        if(self.is_empty()): return False
        cur_node = self.root
        while cur_node != None:
            if(cur_node.val == val): return True
            if(val <= cur_node.val):
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def delete(self, val):
        self.__delete(self.root, val)

    def __delete(self, root, val):
        if(root == None): return root
        if(val < root.val):
            root.left = self.__delete(root.left, val)
        elif(val > root.val):
            root.right = self.__delete(root.right, val)
        else:
            if(root.left == None): return root.right
            elif(root.right == None): return root.left
            else:
                cur = self.__get_inorder_successor(root)
                root.val = cur.val
                root.right = self.__delete(root.right, cur.val)
        return root

    def __get_inorder_successor(self, root):
        cur = root.right
        while cur != None and cur.left != None:
            cur = cur.left
        return cur

    def inorder_traversal(self):
        return self.__inorder_traversal(self.root)
        
    def __inorder_traversal(self, root):
        if(root == None): return []
        return self.__inorder_traversal(root.left) + [root.val] + self.__inorder_traversal(root.right)

    def preorder_traversal(self):
        return self.__preorder_traversal(self.root)
        
    def __preorder_traversal(self, root):
        if(root == None): return []
        return [root.val] + self.__preorder_traversal(root.left) + self.__preorder_traversal(root.right)

    def postorder_traversal(self):
        return self.__postorder_traversal(self.root)
        
    def __postorder_traversal(self, root):
        if(root == None): return []
        return self.__postorder_traversal(root.left) + self.__postorder_traversal(root.right) + [root.val]

    # leetcode : 105
    def build_bt_via_inorder_and_preorder(self, inorder, preorder):
        if(len(preorder) == 0): return None 
        root = Node(preorder[0])
        ri = inorder.index(preorder[0])
        root.left = self.build_bt_via_inorder_and_preorder(preorder[1:ri+1], inorder[:ri])
        root.right = self.build_bt_via_inorder_and_preorder(preorder[ri+1:], inorder[ri+1:])
        return root
    
     # leetcode : 106
    def build_bt_via_inorder_and_postorder(self, inorder, postorder):
        if(len(postorder) == 0): return None 
        root = Node(postorder[len(postorder)-1])
        ri = inorder.index(postorder[len(postorder)-1])
        root.left = self.build_bt_via_inorder_and_postorder(inorder[:ri], postorder[:ri])
        root.right = self.build_bt_via_inorder_and_postorder(inorder[ri+1:], postorder[ri:len(postorder)-1])
        return root
    
    # leetcode : 1008
    def build_bst_from_preorder(self, preorder):
        if(len(preorder) == 0): return  
        root = Node(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
    
    # leetcode : 104
    def find_max_depth(self):
        return self.max_depth(self.root)

    def max_depth(self, root):
        if(root == None): return 0
        maxLeft = self.max_depth(root.left)
        maxRight = self.max_depth(root.right)
        return max(maxLeft, maxRight) + 1
    
    # leetcode : 114
    def has_root_to_leaf_path_sum_of_target(self, target):
        return self.has_path_sum(self.root, target, 0)

    def has_path_sum(self, root, targetSum, fsum):
        if(root == None): return False
        fsum += root.val
        if( root.left == None and root.right == None):
            return targetSum == fsum
        return self.has_path_sum(root.left, targetSum, fsum) or self.has_path_sum(root.right, targetSum, fsum)
    
    def find_len_of_longest_leaf_to_leaf_path(self, root):
        if(root == None): return 0
        left_height = self.max_depth(self.root.left)
        right_height = self.max_depth(self.root.right)
        return max(1+left_height+right_height, max(self.find_len_of_longest_leaf_to_leaf_path(root.left),self.find_len_of_longest_leaf_to_leaf_path(root.right)))
    
    # leetcode : 235
    def lowest_common_ancestor_of_BST(self, root, p, q):
        while root:
            if(p.val < root.val and q.val < root.val): 
                root = root.left
            elif(p.val > root.val and q.val > root.val): 
                root = root.right
            else:
                return root
            
    # leetcode : 236
    def lowest_common_ancestor_of_BT(self, root, p, q):
        if(root == None or root.val == p.val or root.val == q.val): 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if(left and right): return root
        return left if left else right
    
    # leetcode : 98
    def is_valid_BST(self, root):
        return self.is_valid(root, float("-inf"), float("inf"))

    def is_valid(self, root, minr, maxr):
        if(root == None): return True
        if(root.val <= minr or root.val >= maxr): return False
        return self.is_valid(root.left, minr, root.val) and self.is_valid(root.right, root.val, maxr)
    
    # leetcode : 119
    def rightSideView(self, root):
        res = []
        if root:
            queue = [root]
            while queue:
                res.append(queue[-1].val)
                queue = [nxtLvlnode for node in queue for nxtLvlnode in (node.left, node.right) if nxtLvlnode]
        return res

def tryItOut():
    tree = BinarySearchTree()
    tree.insert(15)
    tree.insert(10)
    tree.insert(18)
    tree.insert(4)
    tree.insert(11)
    tree.insert(16)
    tree.insert(20)
    tree.insert(13)
    tree.insert(19)
    tree.insert(21)
    print("Inorder Traversal: ", tree.inorder_traversal())
    print("Preorder Traversal: ", tree.preorder_traversal())
    print("Postorder Traversal: ", tree.postorder_traversal())
    print("Search: ", tree.search(11))
    tree.delete(13)
    print("Delete Inorder Traversal: ", tree.inorder_traversal())
    tree.build_bt_via_inorder_and_preorder([4, 10, 11, 13, 15, 16, 18, 19, 20, 21], [15, 10, 4, 11, 13, 18, 16, 20, 19, 21])
    print("Postorder Traversal: ", tree.postorder_traversal())
    tree.build_bt_via_inorder_and_postorder([4, 10, 11, 13, 15, 16, 18, 19, 20, 21], [4, 13, 11, 10, 16, 19, 21, 20, 18, 15])
    print("Preorder Traversal: ", tree.preorder_traversal())
    print("Max Depth:", tree.find_max_depth())
    print("path Sum: ", tree.has_root_to_leaf_path_sum_of_target(30))
    print("path:  ", tree.find_len_of_longest_leaf_to_leaf_path(tree.root))

tryItOut()
        
