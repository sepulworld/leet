class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class AddTwoNumbers:
    def __init__(self):
        self.integer1 = ""
        self.integer2 = ""
       
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        next_node1 = l1
        next_node2 = l2
       
        while next_node1:
            self.integer1 = str(next_node1.val) + self.integer1
            next_node1 = next_node1.next
       
        while next_node2:
            self.integer2 = str(next_node2.val) + self.integer2
            next_node2 = next_node2.next
               
        list = []
        set_int1 = int(self.integer1)
        set_int2 = int(self.integer2)
        result = set_int1 + set_int2
        for i in str(result):
            list.insert(0, int(i))
        return list
