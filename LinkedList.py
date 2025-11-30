# LINKED LIST 

# class Node():
#     def __init__(self,val):
#         self.data = val
#         self.next  = None

# node1 = Node(5)
# node2 = Node(2)
# node3 = Node(7)
# node4 = Node(4)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# head = node1
# temp = head

# while temp is not None:
#     print(temp.data,"->",end=" ")
#     temp = temp.next
# print("None")


# class Node:
#     def __init__(self,val):
#         self.data = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def traversal(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data,"->",end=" ")
#             temp = temp.next
#         print("None")



## Append and Transvers

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def traverse(self):
#         if not self.head:
#             print("SLL is empty")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next
#             print()

# ssl = SinglyLinkedList()

# ssl.append(10)
# ssl.append(20)
# ssl.append(30)
# ssl.append(40)
# ssl.append(1)

# ssl.traverse()


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        # if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()


    def insert_at(self,val,position):
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = None
            current = self.head
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node Not Found")
    
            

        


    
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(1)
sll.insert_at(5,2)
sll.delete(30)
sll.traverse()


# def insert_at(self, val, position):
#     new_node = Node(val)
      # insertion at 1st index
#     if position == 0:
#         new_node.next = self.head
#         self.head = new_node
      # insertion at a given postion
#     else:
#         current = self.head
#         prev_node = None
#         count = 0
#         while current is not None and count < position:
#             prev_node = current
#             current = current.next
#             count += 1
#         prev_node.next = new_node
#         new_node.next = current