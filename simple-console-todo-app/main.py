class TodoApp:
    def __init__(self):
        tasks = []
        self.items = tasks

        
    def addItems(self, item):
        self.items.append(item)
    
    def getItems(self):
        return self.items
    
    def markCompleted(self, index):
        
        try:
            self.items.pop(index)
        except:
            return -1
        
todo = TodoApp()


menu = "Menu :\nEnter 'a' to add task.\nEnter 'g' to get list of your tasks.\nEnter 'c' to mark the task completed.\nLeave blank and press enter to exit\n"
print(menu)
while True:
   
        
    query = input("> ").lower()
    
    if query == "a":
        while True:
            task = input("Enter task => ")
            todo.addItems(task)
            print("Item added Successfully\n")
            if task == "":
                break
        print(menu)
    
    elif query == "g":
        items = todo.getItems()
        print("=" * 20, "/n")
        
        for item in range(len(items)):
            print(item + 1, ".", items[item])
        print("=" * 20)
        
    elif query == "c":
        items = todo.getItems()
        print("Current Tasks : \n")
        
        for item in range(len(items)):
            print(item+1, ".", items[item])
        
        itemNumber = int(input("Enter the item number to delete the item => "))
        
        result = todo.markCompleted(itemNumber-1)
        
        if result == -1:
            print("Invalid Item Number")
        
        else:
            print("Item removed successfully")
    
    elif query == "":
        exit()
        
    else:
        print("Please enter valid option")
            