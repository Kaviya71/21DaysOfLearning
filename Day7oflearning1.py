print('To add a element at the end')
a=[1,2,5,3,4,5]
a.append(7)
print(a)

print('To merge two list')
b=[7,8,9,0]
a.extend(b)
print(a)

print('To delete a element at specific index:')
c=a
c.pop(1)
print(c)
print('To delete a element at last:')
c.pop()
print(c)

print('To find the length of the list ')
print(len(c))


print('Slicing :')
print(c[1:6:2])
print(c)

print("To count how many times a number occurs in a list")
c.count(5)

