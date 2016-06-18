from doubly import Doubly

w_iterator = 7
terminator = False

obj = Doubly()

while w_iterator > 6 and terminator == False :
    print "1 to add to the start "
    print "2 to add to the end "
    print "3 to remove from start"
    print "4 to remove from end"
    print "5 to insert at index"
    print "6 to remove from index"
    print "7 to print the list"
    print "0 to terminate"

    option = input("enter your option\n")

    if option == 1:
        item = raw_input("enter the item to be inserted \n")
        obj.insert_head(item)
        print "-----------------------------------------"

    elif option == 2:
        item = raw_input("enter the item to be inserted \n")
        obj.insert_tail(item)
        print "-----------------------------------------"

    elif option == 3:
        item = obj.remove_head()
        print "removed head - "+str(item)
        print "----------------------------------------"

    elif option == 4:
        item = obj.remove_tail()
        print "removed tail - "+str(item)
        print "----------------------------------------"

    elif option == 5:
        index = raw_input("enter the index (starts from zero) where item should be inserted \n")
        data = raw_input("What you wanna insert? \n")
        obj.insert_to_index(index , data)
        print "----------------------------------------"

    elif option == 6:
        index = raw_input("enter the index (starts from zero) from which item should be removed \n")
        item  = obj.remove_from_index(index)
        print "item removed - "+item
        print "----------------------------------------"

    elif option == 7:
        s_list = obj.get_list()
        print s_list
        print "----------------------------------------"

    elif option == 0:
        print "programme is terminated"
        print "----------------------------------------"
        terminator = True
