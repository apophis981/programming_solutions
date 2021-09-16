# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
# We are given a list A of unique strings of equal length. How many groups are there?
# Example 1:
# Input: ["tars","rats","arts","star"]
# Output: 2
#

# if diff between two strings is 2 characters and a[i] == b[j] and b[i] == a[j]
# Create a function which determines if strings are similar
# for each item if it is similar to any of the previous strings, remove that string
# return the length of the final array

arr = ["tars","rats","arts","star"]

def compare_strings(str1, str2):
    pass

def check_groups(arr):
    return len(arr)
    pass

print(check_groups(arr))
