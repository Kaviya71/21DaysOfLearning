a1=tuple(map(int,input("Enter the values: ").split()))
print('tuple:',a1)
print("The length of the tuple: ",len(a1))

print("To find the maximum value present in the tuple")
print("The maximum value in the tuple: ",max(a1))
print("To find the minimum value present in the tuple")
print("The minimum value in the tuple: ",min(a1))

b1=list(a1)
print("To append the tuple")
new_value=int(input("Enter the new value: "))
b1.append(new_value)
a2=tuple(b1)
print("The updated tuple after adding a element:",a2)

b2=list(a2)
remove_value=int(input("Enter the value to remove from the list: "))
b2.remove(remove_value)
a3=tuple(b2)
print("The updated tuple after removing a element:",a3)

print("To search a number in a tuple:")
search=int(input("Enter the number to search: "))
if search in a3:
    print("The number is present at the index:",a3.index(search))
else:
    print("The number is not found in the tuple")
           






                 


