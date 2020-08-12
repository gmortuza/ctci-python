from LinkedList import LinkedList


def remove_dups(ll):
    curr = ll.head
    seen = set([curr.val])
    while curr.next:
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            seen.add(curr.next.val)
            curr = curr.next

def remove_dups_followup(ll):
    # run time --> O(n^2)
    # Space --> O(1)
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                # remove this
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


ll = LinkedList()
#ll.generate(100, 0, 9)
#print(ll)
#remove_dups(ll)
#print(ll)

ll.generate(100, 0, 9)
print(ll)
remove_dups_followup(ll)
print(ll)