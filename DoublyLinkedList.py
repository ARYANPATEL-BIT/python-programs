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
#             print(temp , end=" ")
#             temp = temp.next
#         print("")

# DLL = doublyLinkedList()
# DLL.insert_at_beigging(10)
# DLL.insert_at_beigging(20)
# DLL.insert_at_beigging(30)
# DLL.insert_at_beigging(40)
# DLL.Display()