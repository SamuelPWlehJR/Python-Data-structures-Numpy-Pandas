class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def _is_empty(self):
        return len(self.items) == 0


# s = stack()
# s.push("A")
# s.push("B")

# print(s.pop())
# print(s.peek())
# print(s._is_empty())

# testing our stack Class
# s = Stack()
# s.push("Red")
# s.push("Blue")
# s.push("Green")

# print("Top: ", s.peek())
# print("Pop: ", s.pop())
# print("Now Pop: ", s.peek())

# stack of names
# s = Stack()
# s.push("Ali")
# s.push("Fatima")
# s.push("Omar")

# print("Stack: ", s.items)
# s.pop()
# print("After Pop: ", s.items)

# stack of color
colors = Stack()
colors.push("Red")
colors.push("Blue")
colors.push("Yellow")

print("Colors Before Pop: ", colors.items)
print("Top color: ", colors.peek())
colors.pop()
print("Now top: ", colors.peek())

# Push Numbers Then Pop All
nums = Stack()
for n in [1, 2, 3, 4, 5]:
    nums.push(n)
    print("Push: ", n)

print("Now Popping: ")
while not nums._is_empty():
    print(nums.pop())

# stack with strings
print("Stack with strings")
s = Stack()
for word in ["Apple", "Banana", "Cherry"]:
    s.push(word)
    print("Pushed: ", word)
print("Stack now: ", s.items)

print("Pop: ", s.pop())
print("Pop: ", s.pop())
print("Stack after pops:", s.items)

