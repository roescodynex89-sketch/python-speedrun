# List — mutable, ordered
fruits = ["apple", "banana", "mango"]
fruits.insert(1, "grape")     # specific index-এ insert
fruits.extend(["kiwi", "fig"]) # multiple item add
fruits.index("banana")         # position finds
len(fruits)                     # size
fruits[-1]                       # last item (negative indexing)
fruits[1:3]                       # slicing → ["grape", "banana"]
fruits.reverse()
fruits.sort(reverse=True)

