"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-14"
-------------------------------------------------------
"""

from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
       
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
       
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        val = _Queue_Node(deepcopy(value), None)
        
        if self._front is None : 
            self._front = self._rear = val
            
        else : 
            self._rear._next = val
        
        self._rear = val
        self._count += 1 
        
        return deepcopy(value)

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"
        
        curr = self._front
        value = curr._value
        
        curr._next = None
        self._front = curr._next
        
        if self._front is None :
            self._rear = None 
            
        self._count -= 1
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"
        
        value = deepcopy(self._front._value)
        
        return value


    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Equivalent of:
        self.insert(source.remove()), but moves nodes not data.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"
       
  
        node = source._front
        # Update the source queue
        source._count -= 1
        source._front = source._front._next
        
        if source._front is None:
            # Clean up source queue if empty.
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
        assert source._front is not None, "Cannot append an empty queue"
        
        if self._front is None:
            self._front = source._front
            
        else:
            self._rear._next = source._front
        
        self._rear = source._rear
        self._count += source._count
        
        source._front = None
        source._rear = None
        source._count = 0
       
        return 
            
            

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        yes  = True
        while source1._front is not None and source2._front is not None :
            
            if yes is True:
                self._move_front_to_rear(source1)
                yes = not True
            else:
                self._move_front_to_rear(source2)
                yes = True
                
                
        if source1._front is not None:
            self._append_queue(source1)

        if source2._front is not None:
            self._append_queue(source2)
            
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based queue (Queue)
            source2 - an array-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        
        yes  = True
        
        if source1._front is  None or source2._front is  None:
            if source1._front is not None:
                self._append_queue(source1)
    
            if source2._front is not None:
                self._append_queue(source2)
        
        elif source1._front is not None and source2._front is not None :
            
            
            self._move_front_to_rear(source1)
            yes = True
            if source2._front is not None:
                self._move_front_to_rear(source2)
                
                yes = True
            
            
            if yes is True:
                self.combine_r(source1, source2)
                

        
        
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        
        while self._front is not None :
            target1._move_front_to_rear(self)
            
            if self._front is not None:
                target2._move_front_to_rear(self)
            
        
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (recursive algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        
        
        if self._front is  None:
            None
        else :   
      
            append = False
            
            if self._front is not None :
                target1._move_front_to_rear(self)
                append =  not False
                
                if self._front is not None:
                    target2._move_front_to_rear(self)
                    append =  not False
                    
            if append is True:
                target1 , target2 = self.split_alt_r()

        
        return target1, target2


    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        identical = False
        if self._count == target._count : 
        
            while self._front is not None:
                if self._value != target._value :
                    
                    identical = False
                else :
                    identical = True
                    self._front = self._front._next
                    target._front = target._front._next 
                    
        else:
            identical = False

        return identical

    def is_identical_r(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (recursive algorithm)
        Use: b = source.is_identical_r(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        
        
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
