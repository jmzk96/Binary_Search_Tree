from BinaryTree import *
from random import randint


def fill_tree(tree,num_elements =100,max_int=1000):
    for i in range(num_elements):
        cur_element = randint(0,max_int)
        tree.insert_element(cur_element)
    return tree

if __name__ == '__main__':
    tree = binary_search_tree()
    btree = fill_tree(tree)
    btree.return_tree()
    print("tree height:"+str(btree.height()))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
