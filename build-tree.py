#
# Building a tree from inorder and postorder traversals
#

### TREES
class Tree(object):
    def __init__(self, obj=None):
        self.left = None
        self.right = None
        self.data = obj

in_list = [2, 3, 1, 5, 4, 6]
post_list = [3, 2, 5, 6, 4, 1]

def build_tree(in_list, post_list):
    if not in_list:
        return None

    root = post_list[-1]
    root_node = Tree(root)

    pos = in_list.index(root)
    left_in_list = in_list[:pos]
    right_in_list = in_list[pos+1:]

    root_node.left = build_tree(left_in_list, [n for n in post_list if n in left_in_list]) # This part can be improved
    root_node.right = build_tree(right_in_list, [n for n in post_list if n in right_in_list]) # This part can be improved

    return root_node


