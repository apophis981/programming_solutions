#
#  Target Practice 05 - Math
#
#
#  Problem:  Trailing Zeroes
#
#  Prompt:   Given a positive integer, return the number of trailing zeros
#            are present on the factorial of that number.
#
#  Input:    Integer >= 0(n)
#  Output:   Integer
#
#  Example:  n = 10
#
#            trailing_zeros(n) = 2
#
#            n = 27
#
#            trailing_zeros(n) = 6
#
#  Explanation: 10! is 3628800, and so has 2 trailing zeroes
#               27! is 1088886945041835216068000000, and so has 6 trailing zeros
#
#  A straightforward way of solving this problem involves just taking the factorial of your input
#  and dividing by 10 until you run out of trailing zeroes. But what is the major problem with this?
#
#  A good way to start solving this problem is by trying a lot of examples.
#

# Time Complexity: O(log N)
# Auxiliary Space Complexity: O(1)

def trailing_zeroes(n):
    result = 0
    power = 1
    while (n//(5 ** power)) > 0:
        result += (n//(5 ** power))
        power += 1
    return result


#  Problem:  Group Anagrams
#
#  Prompt:   Given an array of words, return an array of arrays of words that
#            groups all anagrams together.
#
#  Input:    words [String]
#  Output:   [[String]]
#
#  Example:  words = ["eat", "tea", "tan", "bat", "ate", "tab", "ant", "tan", "and"]
#
#            group_anagrams(words) =
#
#            [
#               ["ate", "eat", "tea"],
#               ["tan", "nat", "ant"],
#               ["bat", "tab"],
#               ["and"]
#            ]
#
#
#  Note:    All inputs will be lowercase letters
#           The order of groupings does not matter
#           The order of the words in the groupings does not matter
#           The words may not all be the same length
#
#

#  Time Complexity: O(NK)
#  Auxiliary Space Complexity: O(NK)

def assign_chars_to_primes():

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    zip = {}
    for index, char in enumerate(chars):
        zip[char] = primes[index]

    return zip

def group_anagrams(words):
    result = []
    anagram_map = {}

    chars = assign_chars_to_primes()

    def compute_anagram_number(string):
        result = 1
        for i in range(len(string)):
            result *= chars[string[i]]

        return result

    for word in words:
        anagram_num = compute_anagram_number(word)
        if anagram_num not in anagram_map:
            anagram_map[anagram_num] = [word]
        else:
            anagram_map[anagram_num].append(word)

    for num in anagram_map:
        result.append(anagram_map[num])

    return result



# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


from io import StringIO
import sys
import random


# code for capturing print output
#
# directions: capture_print function returns a list of all elements that were
#             printed using print with the function that it is given. Note that
#             the function given to capture_print must be fed using lambda.
#             Example cis provided below
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


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

# compare if two flat lists are equal
def lists_matching(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    cache = {}
    for i in range(0, len(lst1)):
        if lst1[i] in cache:
            cache[lst1[i]] += 1
        else:
            cache[lst1[i]] = 1
    for j in range(0, len(lst2)):
        if lst2[j] not in cache or cache[lst2[j]] == 0:
            return False
        cache[lst2[j]] -= 1
    return True

# Compare if two groups are equal.
def groups_matching(correct_answer, test):
    for i in range(len(correct_answer)):
        contains_group = False
        for j in range(len(test)):
            if (lists_matching(correct_answer[i], test[j])):
                contains_group = True
                break
        if not contains_group:
            return False
    for i in range(len(test)):
        contains_group = False
        for j in range(len(correct_answer)):
            if (lists_matching(test[i], correct_answer[j])):
                contains_group = True
                break
        if not contains_group:
            return False
    return True


print('Trailing Zeros Tests')
test_count = [0, 0]


def test():
    example = trailing_zeroes(10)
    return example == 2


expect(test_count, 'should work on first example input', test)


def test():
    example = trailing_zeroes(27)
    return example == 6


expect(test_count, 'should work on second example input', test)


def test():
    example = trailing_zeroes(0)
    return example == 0


expect(test_count, 'should work on zero', test)


def test():
    example = trailing_zeroes(1037)
    return example == 257


expect(test_count, 'should work on large input', test)


def test():
    example = trailing_zeroes(79204102)
    return example == 19801020


expect(test_count, 'should work on very large input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Group Anagram Tests')
test_count = [0, 0]


def test():
    correct_answer = [["ate", "eat", "tea"], ["tan", "nat", "ant"], ["bat", "tab"], ["and"]]
    test = group_anagrams(["eat", "tea", "nat", "bat", "ate", "tab", "ant", "tan", "and"])
    return groups_matching(correct_answer, test)


expect(test_count, 'should work on example input', test)


def test():
    correct_answer = []
    test = group_anagrams([])
    return groups_matching(correct_answer, test)


expect(test_count, 'should work on empty input', test)


def test():
    correct_answer = [["hello"], ["world"], ["foo"], ["bar"], ["baz"]]
    test = group_anagrams(["hello", "world", "foo", "bar", "baz"])
    return groups_matching(correct_answer, test)


expect(test_count, 'should work on input with no anagrams', test)


print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
