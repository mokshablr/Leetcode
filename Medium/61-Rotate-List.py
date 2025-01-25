import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


inp = json.loads(input())
k = int(input())

def make_list(inp_list):
    nextNode = None
    for i in inp_list[::-1]:
        node = ListNode(i, next = nextNode)
        nextNode = node
        print(i)
    return nextNode

def printLL(head):
    while(head != None):
        print("ELE:", head.val)
        head = head.next
    print("END")

# The only functions to be submitted are below
def lenLL(head):
    count = 0
    while (head != None):
        count += 1
        head = head.next

    return count

def places_to_move(head, k):
    l = lenLL(head)
    if l <1 or k <1 or k==l:
        return 0
    else:
        return 1+l-(k % l)

def rotateRight(head, k):
    if head !=None:
        amt = places_to_move(head, k)
        if amt == 0:
            return head
        forward = head.next
        behind = head
        step = 2
        if forward != None:
            while step < amt:
                forward = forward.next
                behind = behind.next
                step +=1
                print("VAL",behind.val)
            new_head = forward
            behind.next = None
            while forward.next != None:
                forward = forward.next
            forward.next = head
        else:
            new_head = head

        print('NEW HEAD', new_head.val)
        return new_head
    else:
        return None


head = make_list(inp)
if head != None:
    print("HEAD:", head.val)
    printLL(head)
    print("LEN:", lenLL(head))

    new_head = rotateRight(head, k)
    print("NEW HEAD")
    printLL(new_head)






