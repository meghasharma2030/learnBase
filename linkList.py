from operator import ne


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
        headVal = self.linkList
        if(headVal.val == dataVal):
            self.linkList = headVal.next
            headVal = None
            return
        while headVal is not None:
            if(headVal.val == dataVal): break
            prev = headVal
            headVal = headVal.next

        if(headVal == None):
            return
        prev.next = headVal.next
        headVal = None

    def reverseList(self, headVal):
        if(headVal == None or headVal.next == None): return headVal
        resList = self.reverseList(headVal.next)
        headVal.next.next = headVal
        headVal.next = None
        return resList

    def print(self):
        printval = self.linkList
        while printval is not None:
            print(printval.val)
            printval = printval.next
        print("--------")
            
    

egList = LinkList()
egList.insertBeginning(23)
egList.insertBeginning(67)
egList.insertEnd(98)
egList.insertBeginning(45)
# egList.deleteNode(45)
egList.print()
egList.linkList = egList.reverseList(egList.linkList)
egList.print()
print("kength:  ",egList.getLength())