# using push method to add elements to a stack using list append method
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

print(stack)
stack.pop()
print(stack)

letters = []
word = "DOG"
for ch in word:
    letters.append(ch)
    print("stack:", letters)

# using the pop method to reverse a string
letters = ['D', 'O', 'G']
while letters:
    ch = letters.pop()
    print("Popped:", ch)

# mixed data types in stack
stack = []
stack.append(100)
stack.append("Hello world")
stack.append(4.5)
stack.append("Trust me")
print("stack: ", stack)
stack.pop()
print("stack: ", stack)

# using stack as to-do list
todo_list = []
todo_list.append("wash the dishes")
todo_list.append("do my laundry")
todo_list.append("clean my room")
todo_list.append("read python book")
print("To-do list: ", todo_list)

done = todo_list.pop()
print("completed task: ", done)
print("Remaining tasks: ", todo_list)

# checking if stack is Empty
stack = []
if not stack:
    print("stack is Empty")
stack.append(10)
print("stack:", stack)
if stack:
    print("stack is not Empty now!")
