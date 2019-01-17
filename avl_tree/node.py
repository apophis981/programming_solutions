class node(object):

  def __init__(self, key):
    "Construct."
    self._left = None
    self._right = None
    self._bf = None
    self._p = None
    self._key = None
    key = property(fget=lambda self: self._key, doc="The node's key")
    left = property(fget=lambda self: self._left, doc="The node's left child")
    right = property(fget=lambda self: self._right,
                     doc="The node's right child")
    p = property(fget=lambda self: self._p, doc="The node's parent")


def __str__(self):
  "String representation."
  return str(self.key)
