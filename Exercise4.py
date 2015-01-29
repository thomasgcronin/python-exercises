while True:
    print
    print "******************************"
    print "EXERCISE 4 - MENU"
    print "******************************"
    print "1. Write input to file"
    print "2. Write input to screen"
    print "3. Quit"
    print "******************************"
    print

    user_choice = raw_input("Enter your choice [1-3]:")

    if user_choice == "1":
        user_phrase = raw_input("Enter a phrase: ")
        with open("my_file.txt", "w") as f:
            f.write(user_phrase)
        print "You have entered: " + user_phrase

    elif user_choice == "2":
        user_phrase = raw_input("Enter a phrase: ")
        print "You have entered: " + user_phrase

    elif user_choice == "3":
        print "Program is quitting."
        exit()
