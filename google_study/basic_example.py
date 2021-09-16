import unittest

class TestStringMethods(unittest.TestCase):

#    def test_upper(self):
#        self.assertEqual('foo'.upper(), 'FOO')
#
#    def test_isupper(self):
#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())
#
#    def test_split(self):
#        s = 'hello world'
#        self.assertEqual(s.split(), ['hello', 'world'])
#        # check that s.split fails when the separator is not a string
#        with self.assertRaises(TypeError):
#            s.split(2)
    def one_swap(self):
        ans = two_strings('abc', 'acb')
        self.assertEqual(ans, True)

    def no_swap(self):
        ans = two_strings('abc', 'abc')
        self.assertEqual(ans, True)

    def no_swap_one_extra(self):
        ans = two_strings('abc', 'abcc')
        self.assertEqual(ans, True)

    def more_swaps_needed(self):
        ans = two_strings('abcbc', 'bcabc')
        self.assertEqual(ans, False)

    def empty_strings(self):
        ans = two_strings('', '')
        self.assertEqual(ans, True)

    def empty_strings_one_extra(self):
        ans = two_strings('', '1')
        self.assertEqual(ans, True)


if __name__ == '__main__':
    unittest.main()
