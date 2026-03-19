# Implementing a queue with a python List
from collections import deque
queue = []

queue.append("Ali")
queue.append("Ayse")
queue.append("Efe")

print("Queue: ", queue)
queue.pop(0)
print("Queue After Popped: ", queue)

# Dequeue using pop(0) with a List
queue = ['Ali', 'Ayse', 'Efe']
print("Current queue: ", queue)

first = queue.pop(0)
last = queue.pop(-1)  # remove the element at index 2
print("Removed: ", first)
print("Queue now: ", queue)

# using the collections.deque

queue = deque()  # create empty deque as a queue

queue.append("Ali")
queue.append("Ayse")
queue.append("Efe")

print(queue)

print("Dequeue using popleft Method\n")
# Dequeue using popleft()
queue = deque(['Ali', 'Ayse', 'Efe'])

front_person = queue.popleft()
print("Removed: ", front_person)
print("Queue Now: ", queue)

# Summary of Basic Operation
# Collections.deque has been declare from above already so there's no need for declaration here

queue = deque()

# Enqueue
queue.append("X")  # add at rear
queue.append("Y")
print("Current Queue before Popleft: ", queue)

# Dequeue
item = queue.popleft()  # remove from the front

# peek(view front without removing)
front = queue[0]  # only if not empty

# check if empty
empty = (len(queue) == 0)
print("Now Queue After Popleft: ", queue)

# Example 1: Simple Number Queue
# Collections is defined above so there's no need to define here
numbers = deque()

# Enqueue
numbers.append(10)
numbers.append(20)
numbers.append(30)
print("After enqueue: ", numbers)

# Dequeue one number
removed = numbers.popleft()
print("Removed: ", removed)
print("Remaining numbers: ", numbers)

# Example 2: Bank Queue Simulation
# Scenario: people waiting at a bank counter.

bank_queue = deque()

# Arrive Customers
bank_queue.append("Customer 1")
bank_queue.append("Customer 2")
bank_queue.append("Customer 3")
print("Initial Queue at the bank: ", bank_queue)

# first Customers Served
served = bank_queue.popleft()
print("Served: ", served)
print("Queue after Serving: ", bank_queue)

# implementing Our Own Queue Class
# the collection.deque container has been defined above so there's no need to define another container


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            print("Queue is empty, nothing to peek.")
            return None
        return self.items[0]

    def size(self):
        return len(self.items)


bank = Queue()
bank.enqueue("Customer 1")
bank.enqueue("Customer 2")
bank.enqueue("Customer 3")

print("Front element: ", bank.peek())
print("Size: ", bank.size())

# dequeue by removing Customer 1 and 2
print("Dequeue: ", bank.dequeue())
print("Dequeue: ", bank.dequeue())

# checking if the queue is empty(still false)
print("Is empty?", bank.is_empty())

# dequeue by removing Customer 3
print("Dequeue: ", bank.dequeue())
print("Is empty now?", bank.is_empty())


# Queue with user Input
# from collections import deque
queue = deque()
for i in range(3):
    name = input("Enter name: ")
    queue.append(name)
print("People in Queue: ", queue)
print("First to be served: ", queue[0])
