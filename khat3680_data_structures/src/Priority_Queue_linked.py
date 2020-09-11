"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-12"
-------------------------------------------------------
"""

from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next
        

class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        return self._count

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"

        node = source._front
        # Update the source queue
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            source._rear = None

        # Update the target queue
        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._rear._next = None
        self._count += 1
        return



    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        
        
        new_node = _PQ_Node(deepcopy(value),None)
        
        if self._front is None : 
            
            self._front = new_node
            self._rear =  new_node
            new_node._next = None
            
        elif self._front._value > value and self._front._next is not None:
            
            self._front = self._front._next
            
        if self._front._value <= value:
            
            last_node=self._rear
            last_node._next= new_node
            self._rear=new_node 
            
        self._rear._next = None  
        
        self._count+=1
        
        
        return
        """
        
        new_node = _PQ_Node(value, None)
        inserted = False
        if self._front is None:
            self._rear = self._front = new_node

        else:
            curr = self._front
            while self._front is not None  and inserted == False:
                if value >= self._rear._value   :
                    self._rear= new_node
                    new_node._next = self._rear._next 
                    inserted = True
                elif value <= curr._value :
                    curr = new_node
                    new_node._next = curr._next 
                    inserted = True
                else:
                    inserted = False
                    

        self._count += 1        
          
        return  
        
            
    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"
        curr = self._front
        value = curr._value
        
        self._front = curr._next   
        self._rear = self._rear._next
        self._count -=1
        
        return value
    
        

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"
        curr = self._front 
        value = deepcopy(curr._value)
        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()
        
        while self._front is not None and self._front._next is not None:
            target1._move_front_to_rear(self)
            target2._move_front_to_rear(self)
            
        if self._front is not None:
            target1._move_front_to_rear(self)
            
        return target1, target2

        

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        count = 0
        previous = None
        
        current = self._front

        while current is not None and current._value < key:

            count += 1
            previous = current
            
            current = current._next

        if current is None:
            #target1 gets everything 
            target1._front = self._front
            target1._rear = self._rear
            target1._count = self._count

        elif previous is None:
            #target2 gets everything
            target2._front = self._front
            target2._rear = self._rear
            target2._count = self._count

        else:

            previous._next = None

            target1._front = self._front
            target1._rear = previous
            target1._count = count

            target2._front = current
            target2._rear = self._rear
            target2._count = self._count - count

        self._front = None
        self._rear = None
        self._count = 0

        
        return(target1, target2)



    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        while source1._front is not None:
            
            self._move_front_to_rear(source1)
            
        while source2._front is not None:
            
            self._move_front_to_rear(source2)

        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"


        
        
        return None
        


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
