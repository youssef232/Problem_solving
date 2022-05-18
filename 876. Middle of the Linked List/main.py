def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    temp = head
    numOfNodes = 1
    while temp.next != None:
        numOfNodes += 1
        temp = temp.next
    middle = None
    if numOfNodes % 2:
        middle = numOfNodes // 2
    else:
        middle = numOfNodes / 2
    temp = head
    for i in range(int(middle)):
        temp = temp.next
    return temp