# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(9)
l1.next = ListNode(9)

l2 = ListNode(1)
#l2.next = ListNode(3)
#l2.next.next = ListNode(7)

def addTwoNumbers(l1, l2):
    def check_(L):
        if L.val >= 10:
            L.val = L.val % 10
            if L.next is not None:
                L.next.val += 1
                check_(L.next)
            else:
                L.next = ListNode(1)
        elif L.next == None:
            return


    if (l1.next is not None) and (l2.next is not None):

        sums = l1.val + l2.val
        if sums >= 10:
            l1.val = sums%10
            l1.next.val += 1
            print(l1.val)
            addTwoNumbers(l1.next, l2.next)

        else:
            l1.val = sums
            print(sums)
            addTwoNumbers(l1.next,l2.next)
    else:
        if l1.next is None and l2.next is not None:
            l1.next = l2.next
        sums = l1.val + l2.val
        l1.val = sums
        check_(l1)


    return l1

a = addTwoNumbers(l1,l2)
print(a.next.next.val)

