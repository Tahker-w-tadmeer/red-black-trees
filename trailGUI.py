import tkinter as tk
from tkinter import messagebox

from rbtree import RBTree

tree = RBTree()
# Create a new instance of tkinter
window = tk.Tk()

# Set the title of the window
window.title("Dictionary Interface")

# Set the size of the window
window.geometry("300x200")

# Create a label for the text field
label = tk.Label(window, text="Word :")
label.grid(row=1, column=0)

# Create a text field
text_field = tk.Entry(window)
text_field.grid(row=1, column=1, padx=10, pady=5)


# Function to handle button clicks


def button_click(button_num):
    if button_num == 1:
        f = open("dict.txt")
        for line in f:
            tree.insert(line.strip())
        messagebox.showinfo("Info",
                            "Word inserted\n" + "Size:" + str(tree.size()) + "\n" + "Height: " + str(tree.height()))
        f.close()
    elif button_num == 2:
        messagebox.showinfo("Info", "Size: " + str(tree.size()) + "\n" + "Height: " + str(tree.height()))
    elif button_num == 3:
        word = text_field.get()
        if len(word) == 0:
            messagebox.showwarning("Missing Input", "Please Enter a word")
            return
        node = tree.search(word)
        if node:
            messagebox.showinfo("Existing Word", word + " already exists in the dictionary")
        else:
            tree.insert(word)
            messagebox.showinfo("Info",
                                "Word inserted\n" + "Size:" + str(tree.size()) + "\n" + "Height: " + str(tree.height()))
    elif button_num == 4:
        word = text_field.get()
        if len(word) == 0:
            messagebox.showwarning("Missing Input", "Please Enter a word")
            return
        node = tree.search(word)
        if node:
            messagebox.showinfo("Lookup", "Found: " + node.key)
        else:
            messagebox.showinfo("LookUp", "Not Found: " + word)


# Create buttons

button1 = tk.Button(window, text="Load ", width=13, height=3, command=lambda button_num=1: button_click(button_num))
button1.grid(row=4, column=1, padx=5, pady=5)

button2 = tk.Button(window, text="Print Size ", width=13, height=3,
                    command=lambda button_num=2: button_click(button_num))
button2.grid(row=4, column=2, padx=5, pady=5)

button3 = tk.Button(window, text="Insert Word ", width=13, height=3,
                    command=lambda button_num=3: button_click(button_num))
button3.grid(row=5, column=1, padx=5, pady=5)

button4 = tk.Button(window, text="Look Up a word", width=13, height=3,
                    command=lambda button_num=4: button_click(button_num))
button4.grid(row=5, column=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()
