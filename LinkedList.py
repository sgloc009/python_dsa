class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return(self.data)
    def __str__(self):
        return(str(self.data))
    def __eq__(self,obj1):
        return (self.__class__ == obj1.__class__ and self.data == obj1.data and self.next == obj1.next)
            
            
        
class LinkedList:
    def __init__(self,node):
        self.head = node
        self.__curr = node
        
    def add(self,node):
        self.__curr.next = node
        self.__curr = node
    
    def __repr__(self):
        n = self.head
        node_str = ""
        while(n!=None):
            if(n == self.head):
                node_str = node_str + str(n)
            else:
                node_str = node_str + "->" + str(n)
            n = n.next
        return node_str
    
    def __str__(self):
        n = self.head
        node_str = ""
        while(n!=None):
            if(n == self.head):
                node_str = node_str + str(n)
            else:
                node_str = node_str + "->" + str(n)
            n = n.next
        return node_str
        
llist = LinkedList(Node(1))
llist.add(Node(2))
llist.add(Node(3))
llist.add(Node(4))

print(llist)