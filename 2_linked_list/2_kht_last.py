from LinkedList import LinkedList


def kth_to_last(ll, k):

   runner = curr = ll.head
   for _ in range(k):
      if not runner:
         return None
      runner = runner.next

   while runner:
      curr = curr.next
      runner = runner.next

   return curr

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))