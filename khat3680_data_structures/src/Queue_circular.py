"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-20"
-------------------------------------------------------
"""

from copy import deepcopy

class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    
    DEFAULT_SIZE = 10

    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(max_size)
        Use: target = Queue()  # uses default max size
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"
        
        self._max_size = max_size
        self._values = [None] * self._max_size
        self._front = 0
        self._rear = 0
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._values == [None]* self._max_size
            

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        
        return self._count==len(self._values)

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count < self._max_size, "queue is full"
        
        self._values[self._rear]=deepcopy(value)
        self._rear = (self._rear+1)% self._max_size
        self._count+=1
                
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty queue"

        value = self._values[self._front]
        self._values[self._front] = None
        self._front = (self._front+1)%self._max_size
        return value
        
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        value = self._values[self._front]
        return deepcopy(value)
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        j = self._front
        i = 0

        while i < self._count:
            yield self._values[j]
            i += 1
            j = (j + 1) % self._max_size