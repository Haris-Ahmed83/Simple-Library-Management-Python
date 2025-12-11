print("====WELCOME TO OUR LIBRARY====")
Books = ["Hope","Grit","Drive","Edge","Lean"]
while True:
    print("1. View all Books")
    print("2. Add Book")
    print("3. Delete Book")
    print("4. Barrow Book")
    print("5. Exit")
    choose = input("Choose the option:")#view book
    if choose == '1':
        print(f"All book view:{Books}")
#ADD Book
    elif choose == "2":
        while True:
            print("For Adding Enter the Book Name")
            New_book=input("Enter the name of Book that You want to Add:")
            Books.append(New_book)
            print("Sucessfully add new book")
            print(f"All book view:{Books}")
            print("Did you want add more books")
            more=input("Do you want to add new book in libary yes/no:")
            if more.lower() != "yes":
                print("Thanks for coming in over libary")
                break
#Deleting Books             
    elif choose== "3":
        print(f"View all books{Books}")
        remove_book=input("Enter the name of book you want to remove:")
        if remove_book in Books:
            Books.remove(remove_book)
            print("Sucessfully removed the book")
            print(f"updated books{Books}")
        else:
            print("Book not found")
#Barrow book
    elif choose =="4":
        while True:
            print("Which Book you want to barrow")
            print(f"Books{Books}")
            Barrow_book =input("Enter the name of book:")
            if Barrow_book in Books:
                print("Barrow Sucessfully")
                print("did you want to buy another book")
                other_book = input("yes/no").lower()
                if other_book != "yes":
                     print("Thanks for coming in over libary")
                     break
            else:
               print("That book is not in over libary")
#exit         
    else:
        if choose == "5":
            print("exit")
            break
        
            


        

