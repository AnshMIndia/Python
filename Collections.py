import queue
import collections
Tuple=("Red","Green","Blue")
Dictionary = {"Name": "Ansh", "Age": 16, "Class": "XI"}
Stacks=[1,2,3,4,5,6,7,8]
Queues=queue.Queue(3)
Deques=collections.deque("ABCDEF", 10)

Tuple=Tuple.__add__(("Black",))
print(Tuple)
print(Tuple.__contains__("Black"))
print(len(Tuple))

print(Dictionary.items())
print(Dictionary.keys())
Dictionary.update({"Gender": "Male"})
Dictionary["Age"]=17
del Dictionary["Class"]
print(Dictionary)
print(len(Dictionary))
Dictionary.clear()
print(Dictionary)
Stacks.append(9)
Stacks.pop()
print(Stacks)

print(Queues.empty())
Queues.put(1)
Queues.put(2)
Queues.get()
print(Queues.full())

print(Deques)
Deques.append('G')
Deques.extend("H")
Deques.pop()
Deques.appendleft('G')
Deques.extendleft("1")
Deques.popleft()
print(Deques)
