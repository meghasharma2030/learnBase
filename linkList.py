class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.linkList =  None

    def getLength(self):
        len = 1
        headVal = self.linkList
        while headVal.next:
            headVal = headVal.next
            len = len + 1
        return len

    def insertBeginning(self, val):
        newNode = Node(val)
        newNode.next = self.linkList
        self.linkList = newNode

    def insertBetween(self, val, betweenNode):
        newNode = Node(val)
        newNode.next = betweenNode.next
        betweenNode.next = newNode

    def insertEnd(self, val):
        if(self.linkList == None):
            self.linkList = Node(val)
            return
        lastVal = self.linkList
        while lastVal.next:
            lastVal = lastVal.next
        lastVal.next = Node(val)

    def deleteNode(self, dataVal):
        if(self.linkList == None): return self.linkList
        while (self.linkList is not None) and (self.linkList.val == dataVal):
            self.linkList = self.linkList.next
        headVal = self.linkList
        while headVal is not None:
            if(headVal.next != None and headVal.next.val == dataVal):
                headVal.next = headVal.next.next
            else:
                headVal= headVal.next

    def reverseList(self, headVal):
        if(headVal == None or headVal.next == None): return headVal
        resList = self.reverseList(headVal.next)
        headVal.next.next = headVal
        headVal.next = None
        return resList

    def print(self):
        printval = self.linkList
        while printval is not None:
            print(printval.val, end=" ")
            printval = printval.next
        print()
            
def tryItOut():
    egList = LinkList()
    egList.insertBeginning(23)
    egList.insertBeginning(67)
    egList.insertEnd(98)
    egList.insertBeginning(45)
    egList.insertBeginning(50)
    egList.print()
    egList.deleteNode(98)
    # egList.linkList = egList.reverseList(egList.linkList)
    egList.print()
    # print("kength:  ",egList.getLength())

tryItOut()