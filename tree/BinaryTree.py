#encoding:utf-8

import Node

class BinaryTree():

    def __init__(self,root=None,size=None):
        self.root = root
        self.size = size

    def insert(self,value):
        node = Node(data=value)
        if self.root is None:
            root = node
            return
        currentNode = self.root
        while(True):
            if value >= currentNode.data:
