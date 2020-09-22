"""
作者   ：bjx
创建时间   ：2020/8/26  11:25 上午 
文件名称   ：实现迭代协议.PY
开发工具   ：PyCharm
"""
#定义树形结构节点
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    for ch in root.depth_first():
        print(ch)