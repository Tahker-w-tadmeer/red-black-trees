from rbtree import RBTree

tree = RBTree()
f = open("dictionary.txt")
for line in f:
    tree.insert(line.strip())
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


