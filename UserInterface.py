from rbtree import RBTree

tree = RBTree()

while True:
    print("##################")
    print("Enter 1 to load dictionary \nEnter 2 to print Dictionary Size")
    print("Enter 3 to insert word \nEnter 4 to look up a word\nEnter 5 to quit")
    op = input("Enter Operation number: ")
    if op == "1":
        f = open("dictionary.txt")
        for line in f:
            tree.insert(line.strip())
        print("Loaded dictionary")
        f.close()
    elif op == "2":
        print("Size: " + str(tree.size()))
        print("Height: " + str(tree.height()))
    elif op == "3":
        word = input("Enter word you Want to insert: ")
        node = tree.search(word)
        if node:
            print(word + " already exists in the dictionary")
        else:
            tree.insert(word)
            print("Size: " + str(tree.size()))
            print("Height: " + str(tree.height()))
    elif op == "4":
        word = input("Enter word you Want to find: ")
        node = tree.search(word)
        if node:
            print("Found: " + node.key)
        else:
            print("Not Found: " + word)
    elif op == "5":
        print("Thank you ")
        break
    else:
        print("Invalid Character, please enter a number between 1 and 5")

