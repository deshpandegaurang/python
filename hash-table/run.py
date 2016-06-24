from hash_table import HashTable

terminator = False

obj = HashTable()

while terminator == False :

    print "1 to add"
    print "2 to delete"
    print "3 to print"

    print "6 to terminate"

    option = input("enter your option\n")

    if option == 1:
        item = raw_input("enter the item to be inserted \n")
        obj.insert(item)

    elif option == 2:
        item = raw_input("enter the item to be deleted \n")
        print "item deleted - "+obj.delete(item)

    elif option == 3:
        print obj.print_hash_table()

    elif option == 6:
        print "programme is terminated"
        terminator = True

    else:
        print "enter valid option"
