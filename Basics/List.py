from operator import index

nums = [12,23,44,12,44,21,24,56,46,78]

names = ["Sakib","Sadman","Nissan"]

mixedList = [10,"Sakib",23.4,True]

print(nums)
print(names)
print(mixedList)

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])


print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[2:])   # [30, 40, 50]
print(numbers[::-1]) # Reversed list

print(mixedList.append(44))
print(mixedList)
print(mixedList.pop())
print(mixedList.insert(2,"Tarannum"))
print(mixedList)
print(mixedList.index("Sakib"))
print(mixedList.count(12))


