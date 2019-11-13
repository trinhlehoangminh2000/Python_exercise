class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def getDataVal(self, e):
        return e.dataval

    def listprint(self):
        printval = self.headval                     #Start with the first value
        while printval is not None:                 #Iterate through the list
            print (printval.dataval)                
            printval = printval.nextval             #Print value become the .nextval of the printed value
            
    def AtBeginning(self,newdata):                  
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode
        
    def insert(self, val_before, newdata):
        check = self.checkNode(newdata)
        if self.checkNode(val_before) and (check == False):
            if val_before is None:
                print("No node to insert after")
            else:     
                clone = val_before.nextval              #Store the next val of val_before
                val_before.nextval = newdata            #Change the next val of the val_before to the desired data              
                newdata.nextval = clone                 #Change the next val of the added data to the clone value before
        else:
            print('The "val_before" doesnt exist in the linked list or the "new node" has already been existed')

    def checkNodeRecursion(self, val, target):
        if val.nextval is None:
            return False
        else:
            while val.nextval is not None:
                if target.dataval == val.dataval:
                    return True
                    break
                else:
                    self.checkNode(val.nextval, target)        
                
            
    def checkNode(self, target):
        node = self.headval
        while True:
            if node.nextval:
                if node.dataval == target.dataval:
                    return True
                    break
                else:
                    node = node.nextval
            else:
                if node.dataval == target.dataval:
                    return True
                else:
                    break
        else:
            return False


list = SLinkedList()

list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")

e6 = Node("lala")

list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
list.AtEnd("Sun")

list.insert(e2,e3)
list.listprint()
