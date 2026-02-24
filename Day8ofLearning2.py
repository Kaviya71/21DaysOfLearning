book=['python','C program','Java','DSP']
while True:
    print('1.Display all the book')
    print('2.Add the a new book')
    print('3.Remove a book')
    print('4.Check whether a book is available or not')
    choice=int(input("Enter your choice: "))
    if choice==1:
        print('1.Display all the book')
        print(book)
    elif choice==2:
        print('2.Add the a new book')
        new_book=input("Enter a new book name")
        book.append(new_book)
        print(book)
    elif choice==3:
        print('3.Remove a book')
        remove_book=input("Enter the book to remove: ")
        if remove_book in book:
            book.remove(remove_book)
        print(book)
    elif choice==4:
        print('4.Check whether a book is available or not')
        check_book=input("Enter a book to check in the list: ")
        if check_book in book:
            print("The book is available")
        else:
            print("The bok is not available")
    else:
        print("Invalid choice")
    
    
    
    
