def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    array = []
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
    
    

