import unittest

class OddTests(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(max_odd([]), None)

    def test_one_element(self):
        self.assertEqual(max_odd([7]), 7)

    def test_one_even(self):
        self.assertEqual(max_odd([2]), None)

    def test_multiple_odd(self):
        self.assertEqual(max_odd([2,7,7,11,8,9,2,1]), 11)

    def test_multiple_even(self):
        self.assertEqual(max_odd([2,4,6,10,8,2]), None)



def max_odd(arr):
    if len(arr) < 1:
        return None
    if len(arr) == 1 and arr[0] % 2 == 0:
        return None
    max = None
    for cur in arr:
        if cur % 2 != 0:
            if max == None or max < cur:
                max = cur
    return max

if __name__ == '__main__':
    unittest.main()
