"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3: 

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

"""

"""
corner cases: no nodes in LL, one node in LL, could you have 1 node that points to itself?
if you have more than one node, you couldn't have a node point to itself, then list wouldn't be linked

brute force idea: loop through list with a count, if the loop exceeds count, the list has a cycle

that won't work, how do you know how many nodes there are?

loop through list, check if the node pointer is in hash table, if it isn't, insert it into hash table, if it is, return true

if you get through list, return false

"""

def cycle(head):
    if head == None:
        return False
    
    H = {}

    node = head

    index = 0

    while node != None:
        if H.get(node) == None:
            H[node] = index
        else:
            return True
        node = node.next
        index += 1

    return False

"""
O(n) time
O(n) space

Best algorithm is Floyd's cycle finding algorithm

# Function that returns true if there is a loop in linked
# list else returns false.
def detect_loop(head):

    # Fast and slow pointers initially points to the head
    slow_p = head
    fast_p = head

    # Loop that runs while fast and slow pointer are not
    # None and not equal
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        # If fast and slow pointer points to the same node,
        # then the cycle is detected
        if slow_p == fast_p:
            return True
    return False

# Driver code
"""