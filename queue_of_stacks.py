# Task
# - Implement a Queue using Stacks


# Example:
# >>> a = Stack()
# >>> a.push(1)
# >>> a.push(2)
# >>> a.push(3)
# >>> a.pop()
#   3
# >>> a.pop()
#   2
# >>> a.pop()
#   1
# >>> a.pop()
#   IndexError: list index out of range

# enqueue()
# dequeue()

class Queue:
    def __init__(self):
        self.items = Stack()
        self.temp = Stack()

    def enqueue(n):
           self.items.push(n)

    def dequeue():
        latest = None
        while len(self.items) >=1:
            latest = self.items.pop()
            if len(self.items) > 1:
                self.temp.push(lastest)
        while len(self.temp) >=1:
            latest2 = self.temp.pop()
            self.items.push(lastest2)
        return(latest)


# a = Queue()
# a.enqueue(1)
# >>> a.enqueue(1)
# >>> a.enqueue(2)
# >>> a.enqueue(3)
# >>> a.dequeue()
# 1


# Optimizing the solution above

class Queue:
    def __init__(self):
        self.items = Stack()
        self.temp = Stack()
        self.ft = True

    def enqueue(n):
           self.items.push(n)

    def dequeue():
        latest = None
        if self.ft:
            self.items, self.temp = self.translate(self.items, self.temp)
            self.ft = False
        else:
            # in case temp is empty refill it with items from self.items
            if len(self.temp) < 1:
                self.items, self.temp = self.translate(self.items, self.temp)
            latest = self.temp.pop()

        return(latest)

   def translate(s1, s2):
        while len(s1) >=1:
            latest = s1.pop()
            if len(s1) > 1:
                s2.push(lastest)
        return(s1,s2)


# a = Queue()
# a.enqueue(1)
# >>> a.enqueue(1)
# >>> a.enqueue(2)
# >>> a.enqueue(3)
# >>> a.dequeue()
# 1
temp [2, 3]
# >>> a.enqueue(1)
temp[2,3]
items[1]
# >>> a.dequeue()
# 2
