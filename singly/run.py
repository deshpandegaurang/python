from singly import Singly

w_iterator = 7
terminator = False

obj = Singly()

while w_iterator > 6 and terminator == False :
    print "1 to add to the start "
    print "2 to add to the end "
    print "3 to remove from start"
    print "4 to remove from end"
    print "5 to print the list"
    print "6 to terminate"

    option = input("enter your option\n")

    if option == 1:
        item = raw_input("enter the item to be inserted \n")
        obj.insert_head(item)

    elif option == 2:
        item = raw_input("enter the item to be inserted \n")
        obj.insert_tail(item)

    elif option == 3:
        item = obj.remove_head()
        print "removed head - "+str(item)

    elif option == 4:
        item = obj.remove_tail()
        print "removed tail - "+str(item)

    elif option == 5:
        s_list = obj.get_list()
        print s_list

    elif option == 6:
        print "programme is terminated"
        terminator = True
