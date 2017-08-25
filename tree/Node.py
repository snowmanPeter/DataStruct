#encoding:utf-8


class Node():
    """
    定义数据库中的节点信息
    """

    def __init__(self,data = None,childNode=None):
        self.data = data
        self.childNode = childNode

    def __init__(self,data = None):
        self.data = data

