from .nodes import node

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert_element(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert_element(value,self.root)

    def _insert_element(self,value,current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = node(value)
            else:
                self._insert_element(value,current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
            else:
                self._insert_element(value,current_node.right_child)
        else:
            print("Value already in tree")

    def return_tree(self):
        if self.root != None:
            self._return_tree(self.root)

    def _return_tree(self,current_node):
        if current_node != None:
            self._return_tree(current_node.left_child)
            print(str(current_node.value))
            self._return_tree(current_node.right_child)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,current_node,current_height):
        if current_node == None:
            return current_height
        left_height = self._height(current_node.left_child,current_height+1)
        right_height = self._height(current_node.right_child,current_height+1)
        return max(left_height,right_height)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,current_node):
       if value == current_node.value:
           return True
       elif value < current_node.value and current_node.left_child != None:
           return self._search(value,current_node.left_child)
       elif value > current_node.value and current_node.right_child != None:
           return self._search(value,current_node.right_child)
       else:
           return False
