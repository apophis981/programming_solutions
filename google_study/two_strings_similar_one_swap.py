# Write a function which takes two strings as input and returns a boolean
# if words can be made equal with a single character swap.
# If 1 character is missing or swapped, return True

import unittest

class TwoStringsTests(unittest.TestCase):
#    def test_one_swap(self):
#        ans = two_strings('abc', 'acb')
#        self.assertEqual(ans, True)
#
#    def test_no_swap(self):
#        ans = two_strings('abc', 'abc')
#        self.assertEqual(ans, True)
#
#    def test_no_swap_one_extra(self):
#        ans = two_strings('abc', 'abcc')
#        self.assertEqual(ans, True)
#
#    def test_no_swap_two_extra(self):
#        ans = two_strings('abc', 'abccc')
#        self.assertEqual(ans, False)

    def test_short_beginning(self):
        ans = two_strings('abc', 'aabc')
        self.assertEqual(ans, True)

#    def test_more_swaps_needed(self):
#        ans = two_strings('abcbc', 'bcabc')
#        self.assertEqual(ans, False)
#
#    def test_empty_strings(self):
#        ans = two_strings('', '')
#        self.assertEqual(ans, True)
#
#    def test_empty_strings_one_extra(self):
#        ans = two_strings('', '1')
#        self.assertEqual(ans, True)
def two_strings(str1, str2):
    if str1 == str2:
        return True
    if abs(len(str1)-len(str2)) > 1:
        print("here")
        return False

    index = 0
    first_diff = []
    second_diff = []

    for index in range(min(len(str1),len(str2))):
        if str1[index] != str2[index]:
            if len(first_diff) > 2:
                return False
            elif len(first_diff) == 0:
                first_diff.append(str1[index])
                second_diff.append(str2[index])
            else:
                first_diff.append(str1[index])
                second_diff.insert(0, str2[index])
    if first_diff != second_diff:
        print(first_diff, second_diff)
        return False
    return True

if __name__ == '__main__':
	unittest.main()
