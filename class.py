class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
root=None
a=[1,10,11,8,6,12,14,7]
# for val in a:
#     print(val)
print(root)
root=Node(a[0])   #object#
print(root)
print(root.data)
b=Node(a[1])   #object#
print(b)
print(b.data)
