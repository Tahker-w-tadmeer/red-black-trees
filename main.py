from rbtree import RBTree
#update on our lab project
tree = RBTree()
f = open("dictionary.txt")
for line in f:
    tree.insert(line)
f.close()

print("Before Insertion: ")
print("Size: " + str(tree.size()))
print("Height: " + str(tree.height()))

tree.insert("Tadmeer")

print("\nAfter Insertion: ")
print("Size: " + str(tree.size()))
print("Height: " + str(tree.height()))

words = ["hello", "fdsf", "Tadmeer", "work", "dfgghjdc"]

for word in words:
    node = tree.search(word)
    if node:
        print("Found: " + node.key)
    else:
        print("Not Found: " + word)


