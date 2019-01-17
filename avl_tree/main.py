#! /usr/bin/python
if '__main__' == __name__:
    import node
    import tree
    import os
    import sys
    import numpy.random as R

def write_tree(t, filename):
    "Write the tree as an SVG file."
    f = open('%s.dot' % filename, 'w')
    write_tree_as_dot(t, f)
    f.close()
    os.system('dot %s.dot -Tsvg -o %s.svg' % (filename, filename))
# test the avltree
R.seed(2)
size = 50
keys = R.randint(-50, 50, size=size)
t = tree.avltree()
test_tree(t, keys)
write_tree(t, 'tree')
