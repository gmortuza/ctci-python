from LinkedList import LinkedList


def partition(ll, x):

    curr = ll.tail = ll.head
    while curr:
        nextNode = curr.next
        curr.next = None
        if curr.val < x:
            # make this as head
            curr.next = ll.head
            ll.head = curr
        else:
            # make this as tail
            ll.tail.next = curr
            ll.tail = curr
        curr = nextNode


if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(100, 0, 50)
    print(ll)
    partition(ll, 25)
    print(ll)

