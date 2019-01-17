# range([start], stop, [step])
list = [0, 1, 2]
# iterate through list
for i in range(len(list)):
    print(list[i])

# Two parameters (start, stop) output: 3, 4, 5
for i in range(3,6):
    print(i)

# Three parameters (start, stop, step) output: 1, 3, 5, 7
for i in range(1, 8, 2):
    print(i)

# Count backwards (start, stop, step) output: 8, 6, 4
for i in range(8, 2, -2):
    print(i)
