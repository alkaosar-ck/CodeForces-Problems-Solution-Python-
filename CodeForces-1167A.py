class Node:
   def __init__(self,head,next = None) -> None:
      self.head = head
      self.next = next
      
def count_len(head):
   total = 0
   current = head
   while current:
      total+=1
      current = current.next
   print(total)
   
def create_linked_list(s):
   head = Node(s[0])
   current = head
   for char in s[1:]:
      new_node = Node(char)
      current.next = new_node
      current = new_node
   return head

def solve(n,s):
   head = create_linked_list(s)
   current = head
   index = 0
   while current:
      if current.head == '8':
         remaining = n-index
         if remaining>=11:
            print('YES')
            return
      current = current.next
      index+=1
   print('NO')

for _ in range(int(input())):
   n = int(input())
   s = input().strip()
   solve(n,s)
   
      
   