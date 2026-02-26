print("Room allotement system")
total_rooms=tuple(map(int,input("Enter the total rooms present: ").split()))
alloted_rooms=tuple(map(int,input("Enter the rooms allocated: ").split()))

if total_rooms not in alloted_rooms:
    print("The rooms which are available are: ",tuple(total_rooms))
else:
    print("All the rooms are allocated")
capacity=int(input("Enter the capacity of the room: "))
vacancy=0
for room in alloted_rooms:
    members=int(input(f"Enter the members in the allocated room {room}:"))
    vacancy=capacity-members
    print("Room",room,"vacancy:",vacancy)
