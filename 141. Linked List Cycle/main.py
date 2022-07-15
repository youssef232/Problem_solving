def hasCycle(self, head: Optional[ListNode]) -> bool:
    mydict = {}
    pointer = head
    while pointer:
        if pointer not in mydict:
            mydict[pointer] = None
            pointer = pointer.next
        else:
            return True

    return False

# another solution
# https://www.youtube.com/watch?v=gBTe7lFR3vc
def hasCycle(self, head: Optional[ListNode]) -> bool:
       slow, fast = head, head
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           if slow == fast:
               return True

       return False