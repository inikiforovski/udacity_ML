import math
import Queue
import numpy as np


class AVLNode:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.bf = 0

    def bfs(self):
        q = Queue.Queue()
        q.put(self)
        # output_str = ''
        output_arr = np.zeros((self.height + 1, pow(2, self.height)))
        i = 0
        j = 0

        print output_arr.shape
        # print output_arr[1][1]

        while not q.empty():
            node = q.get()
            if node is not None:
                if node.left is not None:
                    q.put(node.left)
                else:
                    q.put(None)
                if node.right is not None:
                    q.put(node.right)
                else:
                    q.put(None)

                # Write to 2d array
                if node is None:
                    output_arr[i][j] = None
                else:
                    output_arr[i][j] = node.key

            # Increment row or col of array as needed
            if j == pow(2, i) - 1:
                i += 1
                j = 0
            else:
                j += 1

            # output_str += str(node.key) + ' '
        return output_arr


def insert_node(root, b):
    if root is None:
        root = b
        if root.parent is not None:
            if root.parent.left == root:
                root.parent.lbf += 1
            else:
                root.parent.rbf += 1
    else:
        if b.key < root.key:
            insert_node(root.left, b)
        else:
            insert_node(root.right, b)
        rebalance_tree(root)


def transplant(root, u, v):
    if u.parent is None:
        root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right == v
    if v is not None:
        v.parent = u.parent
    return root


def right_rotate(root, x):
    y = x.left
    root = transplant(root, x, y)
    x.left = y.right
    if x.left is not None:
        x.left.parent = x
    y.right = x
    x.parent = y
    x.height = max(x.left.height, x.right.height) + 1
    x.bf = x.right.height - x.left.height
    y.height = max(y.left.height, y.right.height) + 1
    y.bf = y.right.height - y.left.height


def insert(x, z):
    if x is None:
        x = z
    elif z.key < x.key:
        x.left = insert(x.left, z)
        x.left.parent = x
        update_height(x)
    else:
        x.right = insert(x.right, z)
        x.right.parent = x
        update_height(x)
    return x


def update_height(z):
    while z is not None:
        lh = 0
        rh = 0
        if z.left is not None:
            lh = z.left.height
        if z.right is not None:
            rh = z.right.height
        if z is not None:
            z.height = max(lh, rh) + 1
        z = z.parent


def print_tree(root):
    if root is None:
        return ''
    else:
        newline = ''
        if root.key == find_max(find_root(root), root.height):
            newline = '\n'
        return str(root.key) + newline + print_tree(root.left) + ' ' + print_tree(root.right)

def print_bfs(z):
    str = np.zeros((1,np.size(z,0)))
    for i in range(np.size(z,0)):
        for j in range(pow(2,i)):
            str[i] += str(z[i][j]).ljust(pow(np.))



def find_root(u):
    if u.parent is not None:
        find_root(u.parent)
    else:
        return a


def find_max(u, level=None):
    if level is None:
        level = 999  # need to change to math.inf
    if u.height < level:
        if u.right is not None:
            return find_max(u.right, level)
        else:
            return u.key
    else:
        return u.key


a = AVLNode(5)
b = AVLNode(6)
c = AVLNode(4)

insert(a, b)
insert(a, c)
insert(a, AVLNode(1))

# print a.left.key
# print a.right.key
# print find_max(c, 0)
print

print a.height
print b.height
print c.height

print c.left.key

print a.bfs()

# print print_tree(a)

# zzz22
