# Real Life uses 
# 1. music Player
# 2. Undo/Redo
# 3. Browser

# disadvantages 
# 1. Extra Space
# 2. MOre Complexe

# Insertion at the beginning

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#         self.prev = None

# class doublyLinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_beigging(self,val):
#         new_node = Node(val)

#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
        
#     def display(self):
#         temp = self.head

#         # while temp
#         while temp.next is not None:
#             print(temp.val , end=" ")
#             temp = temp.next
#         print("")

# DLL = doublyLinkedList()
# DLL.insert_at_beigging(10)
# DLL.insert_at_beigging(20)
# DLL.insert_at_beigging(30)
# DLL.insert_at_beigging(40)
# DLL.display()


# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_head(self,val):
#         new_node = Node(val)

#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
    
#     def insert_at(self,val,position):
#         new_node = Node(val)

#         if position == 0:
#             if self.head:
#                 new_node.next = self.head
#                 self.head.prev = new_node
#             self.head = new_node
#             return
        
        
        
#         current = self.head 
#         count = 0
#         while count < position - 1 and current:
#             current = current.next 
#             count += 1
            
#         if current is None:
#             print("Position out of bound")
#             return
            
#         new_node.next = current.next
#         new_node.prev = current
#         if current.next:
#             current.next.prev = new_node
#         current.next = new_node

#     def printValues(self):
#         if self.head is None:
#             print("Doubly Linked List is empty")
        
#         current = self.head
#         while current:
#             print(current.val,end=" ")
#             current= current.next
#         print()

    
# dll = DoublyLinkedList()
# dll.insert_at(10,0)
# dll.insert_at(20,1)
# dll.insert_at(30,2)
# dll.insert_at(40,3)
# dll.insert_at(50,4)
# dll.printValues()
# dll.insert_at_head(5)
# dll.printValues()
# dll.insert_at(25,3)
# dll.printValues()


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at(self,val ,position):
        new_node = Node(val)
        
        if position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return
        
        else:
            count = 0 
            current = self.head
            while count < position -1 and current:
                current = current.next
                count += 1
            
            if  current is None:
                print("Position out of bound")
                return
            
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def delete_head(self):
        if self.head is None:
            return
        
        if not self.head.next:
            self.head = None
            return
        
        self.head = self.head.next 
        self.head.prev = None

    def delete_last(self):
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next.prev = None
            current.next = None
        
    # def deletion(self,val):

    #     if self.head is None:
    #         return
        
    #     current = self.head
    #     while current and current.val != val:
    #         current = current.next
        
    #     if current is None:
    #         print("Node not Found")
    #         return
        
    #     if current == self.head:
    #         if self.head.next is None:
    #             self.head = None
    #             return
    #         self.head = self.head.next
    #         self.head.prev = None
    #         return
        
    #     if current.next is not None:
    #         current.prev.next = current.next
    #         current.next.prev = current.prev
    #     else:
    #         current.prev.next = None
        

    def deletion(self,val):

        if self.head is None:
            return
        
        current = self.head
        while current and current.val != val:
            current = current.next
        
        if current is None:
            print("Node not Found!")
            return
        
        if current == self.head:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = self.head
                return
        
        if current.next is not None:
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            current.next.prev = None
        
        
        


    def traverse(self):
        if self.head is None:
            print("Doubly LinkedList is Empty")
        
        else:
            current = self.head
            while current:
                print(current.val,end=" ")
                current = current.next
            print()

dll = DoublyLinkedList()
dll.insert_at(10,0)
dll.insert_at(20,1)
dll.insert_at(30,2)
dll.insert_at(40,3)
dll.insert_at(50,4)
dll.traverse()
dll.insert_at_head(5)
dll.traverse()
dll.insert_at(25,3)
dll.traverse()
dll.delete_head()
dll.traverse()
dll.delete_last()
dll.traverse()
dll.deletion(20)
dll.traverse()