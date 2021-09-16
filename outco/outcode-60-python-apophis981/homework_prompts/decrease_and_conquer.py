# Kth Largest: Given a unsorted array and an integer k, find the kth largest element in the array

# Parameters
# Input: arr (ints) Input: k (int)
# Output: int

# Constraints k < length of arr
# Time: O(N)
# Space: O(N)

# [1, 4, 2, 5, 12, 9], 3 --> 5
# [4, 7, 1, 6], 1 --> 7
# [6, 44, 2, 1, 9, 10, -1, 78, 90], 3 --> 44


def kth_largest(k, arr):
    # YOUR WORK HERE
    pass


# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


from io import StringIO
import sys
import random


# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


# compare if two flat lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


print('\nKth_Largest')
test_count = [0, 0]

def test():
    example = kth_largest(3, [1, 4, 2, 5, 12, 9])
    return example is not None and example == 5

expect(test_count, "return correct value for 3rd largest value in the array", test)

def test():
    example = kth_largest(1, [4, 7, 1, 6])
    return example is not None and example == 7

expect(test_count, "returns correct value for largest value in the array", test)

def test():
    example = kth_largest(9, [6, 44, 2, 1, 9, 10, -1, 78, 90])
    return example is not None and example == -1

expect(test_count, "returns correct value for smallest value in the array", test)
