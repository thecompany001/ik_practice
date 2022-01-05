def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    array = []
    for linkedlist in lists:
        current = linkedlist
        while current is not None:
            array.append(current.data)
            current = current.next
            
    arrays.sort()
    
    if len(arrays) == 0:
        return None
    
    head = SinglyLinkedListNode(node_data=arrays[0])
    current = head
    
    for item in arrays[1:]:
        next_node = SinglyLinkedListNode(node_data=arrays[0])
        current.next = next_node
        current = current.next
        return head
        
        
XXXX

def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    arrays = []
    for linkedlist in lists:
        current = linkedlist
        while current is not None:
            arrays.append(current.data)
            current = current.next
            
    arrays.sort()
    
    if len(arrays) == 0:
        return None
        
    head = SinglyLinkedListNode(node_data=arrays[0])
    current = head
    for item in arrays[1:]:
        next_node = SinglyLinkedListNode(node_data=item)
        current.next = next_node
        current = current.next
    return head


XXXX


def merge_k_lists(lists):
    if len(lists) <= 0:
        return lists
    arr = []
    for innerList in lists:
        current = innerList
        while current is not None:
            arr.append(current.data)
            current = current.next
    arr.sort()
    if len(arr) <=0:
        return None
    start = SinglyLinkedListNode(node_data = arr[0])
    current = start
    for item in arr[1:]:
        next_data = SinglyLinkedListNode(node_data = item)
        current.next = next_data
        current = current.next
    return start
    
XXXX

def merge_k_lists(lists):

    all_nodes = []
    head = ll = SinglyLinkedListNode(0)
    for l in lists:
        while l:
            all_nodes.append(l.data)
            l = l.next
    for x in sorted(all_nodes):
        ll.next = SinglyLinkedListNode(x)
        ll = ll.next
    return head.next


XXXX

import heapq

def merge_k_lists(lists):
    
    heapq_arr = []
    
    for l in lists:
        head = l
        while head is not None:
            heapq.heappush(heapq_arr, head.data)
            head = head.next
    
    head = point = SinglyLinkedListNode(0)
    
    while len(heapq_arr) > 0:
        popped = heapq.heappop(heapq_arr);
        point.next = SinglyLinkedListNode(popped)
        point = point.next
        
    return head.next

XXXX

import heapq

def merge_k_lists(lists):
    pq = []
        
    # Put each element from each linked list into priority queue
    for linkedlist in lists:
        while linkedlist is not None:
            heapq.heappush(pq, linkedlist.data)
            linkedlist = linkedlist.next
    
    # PQ should now be populated with all values satisfying heap order
    # Construct new LL
    
    dummy_head = SinglyLinkedListNode(None)
    curr = dummy_head
    
    while pq:
        next_smallest = heapq.heappop(pq)
        curr.next = SinglyLinkedListNode(next_smallest)
        curr = curr.next
    
    return dummy_head.next

XXXX

def merge_k_lists(lists):
    if (len(lists) <= 0):
        return lists
    a =[]
    for list in lists:
        c = list
        while c is not None:
            a.append(c.data)
            c = c.next
    a.sort()
    if (len(a) <= 0):
        return None
    start = SinglyLinkedListNode(a[0])
    c = start
    for i in range(1,len(a)):
        nextdata = SinglyLinkedListNode(node_data=a[i])
        c.next = nextdata
        c = c.next
    return start