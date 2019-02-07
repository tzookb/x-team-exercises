class Item:
    def __init__(self, count):
        self.count = count
        self.nexts = {}

def insert_contact(item, user):
    curSpot = item
    for char in list(user):
        if char not in curSpot.nexts:
            curSpot.nexts[char] = Item(0)
        
        curSpot.nexts[char].count += 1
        curSpot = curSpot.nexts[char]


def find_partial(item, partial):
    curSpot = item
    for char in list(partial):
        if char not in curSpot.nexts:
            return 0
        curSpot = curSpot.nexts[char]
    
    return curSpot.count

def contacts(queries):
    users = Item(0)

    for query in queries:
        action = query[0]
        item = query[1]
        if action == "add":
            insert_contact(users, item)
        else:
            res = find_partial(users, item)
            print(res)


contacts([
    ["add", "hack"],
    ["add", "hackerrank"],
    ["find", "hac"],
    ["find", "hak"],
])
