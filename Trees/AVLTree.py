'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files.
'''

from Trees.BinaryTree import BinaryTree, Node
from Trees.BST import BST
# from BinaryTree import BinaryTree, Node
# from BST import BST

class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''

        BST.__init__(self,xs)

        # self.root = None
        # if xs:
        #     self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)


    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)


    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''

        return (AVLTree._balance_factor(node) in [-1,0,1])

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''

        if node is None or node.right is None:
            return node

        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        return new_node


    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''

        return
    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        return


# avltree0 = AVLTree()
# avltree0.root = Node(5)
# avltree0.root.left = Node(3)
# avltree0.root.left.left = Node(1)
# avltree0.root.right = Node(7)
#
# avl = AVLTree()
#
#
# # print(avltree0.is_avl_satisfied())
# avltree4 = AVLTree()
# avltree4.root = Node(5)
# avltree4.root.left = Node(3)
# avltree4.root.left.left = Node(1)
# avltree4.root.left.right = Node(4)
# avltree4.root.right = Node(7)
# avltree4.root.right.left = Node(6)
# avltree4.root.right.right = Node(9)
#
# print(AVLTree._left_rotate(avltree4.root))