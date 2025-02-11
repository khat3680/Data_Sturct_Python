from copy import deepcopy

class Stack:
    """
    -------------------------------------------------------
    Implementation of Stack ADT (Array-based Implementation)
    Top of Stack is the first element in the Python list
    -------------------------------------------------------
    """ 
    def __init__(self,size):
        """
        -------------------------------------------------------
        Description:
            Initializes a Stack Object
            Initializes items to an empty list
            A stack has a cap which is defined by the given size
        Use: stack = Stack()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            A Stack object (Stack)            
        -------------------------------------------------------
        """
        self.items = []
        self.size = size
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of top of stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.peek()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An item from top of stack (?)            
        -------------------------------------------------------
        """
        result = None
        if self.is_empty():
            print('Error(Stack.peek):Invalid peek operation. Stack is empty')
        else:
            result = deepcopy(self.items[0])
        return result

    def push(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the stack
        Use: stack.push(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the stack (?)
        Returns:
            None           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(Stack.push):Invalid push operation. Stack is full')
        else:
            self.items.insert(0,deepcopy(item))
        return
    
    def pop(self):
        """
        -------------------------------------------------------
        Description:
            Removes the top item of the stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.pop()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Stack.pop):Invalid pop operation. Stack is empty')
            return None
        item = deepcopy(self.items[0])
        del self.items[0]
        return item
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if stack is empty
        Use: result = stack.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self.items)== 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if stack is full
            A stack is full when number of items equal to stack size
        Use: result = stack.is_full
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if stack is full, False otherwise
        -------------------------------------------------------
        """
        return len(self.items)== self.size
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Stack ADT
            Prints all items in stack
            prints [] if stack is empty
        Use: stack.print()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        -------------------------------------------------------
        """
        if self.is_empty():
            output =  '[]'
        else:
            output = ''
            for i in range(len(self.items)):
                output = output + str(self.items[i])
                if i != len(self.items) -1:
                    output+='\n'
        return output

class Queue:
    """
    -------------------------------------------------------
    Implementation of Queue ADT (Array-based Implementation)
    start of Queue is the last element in the Python list
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self,size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Description:
            Initializes a Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            A Queue object (Queue)            
        -------------------------------------------------------
        """
        assert isinstance(size,int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        self._items = []
        self._size = size
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Queue.peek): Invalid peek operation. Queue is empty')
            return None
        return deepcopy(self._items[-1]) 
    
    def insert(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the rear of the queue
        Use: queue.insert(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(Queue.insert): Invalid insert operation. Queue is full')
        else:
            self._items.insert(0,deepcopy(item))
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the first item of in the queue,
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Queue.remove):Invalid remove operation. Queue is empty')
            return None
        return deepcopy(self._items.pop(-1))
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = queue.is_empty()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._items)== 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = queue.is_full()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return len(self._items) == self._size
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Override built-in len() method
            Returns number of items currently in queue
        Use: num = len(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return len(self._items)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints all items in Queue
            (First Second ... Last)
            prints () if queue is empty
        Use: str(queue) 
             print(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if self.is_empty():
            output =  '()'
        else:
            output = '('
            for i in range(len(self._items)-1,-1,-1):
                output = output + str(self._items[i])+' '
        output = output[:-1]+')'
        return output

class cQueue:
    """
    -------------------------------------------------------
    Implementation of Circular Queue ADT (Array-based Implementation)
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self,size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Description:
            Initializes a Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: cq = cQueue()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            A Queue object (Queue)            
        -------------------------------------------------------
        """
        assert isinstance(size,int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        self._max_size = size
        self._current_size = 0
        self._items = [None]*size
        self._front = -1
        self._rear = -1

    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = cq.peek()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(cQueue.peek):Invalid peek operation. Queue is empty')
            return None
        return deepcopy(self._items[self._front])
    
    def insert(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the queue
        Use: cq.insert(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(cQueue.insert): Invalid insert operation. Queue is full')
            return
        
        if self.is_empty():
            self._front = self._max_size - 1
            self._rear = self._max_size - 1
        else:
            self._rear = (self._rear-1)%self._max_size
        
        self._items[self._rear] = deepcopy(item)
        self._current_size +=1
        
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the first item of in the queue,
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = cq.remove()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(cQueue.remove):Invalid remove operation. Queue is empty')
            return None
        
        removed_item = deepcopy(self._items[self._front])
        self._items[self._front] = None

        self._current_size-=1
        
        if self._current_size == 0:
            self._front = -1
            self._rear = -1
        else:
            self._front = (self._front - 1)%self._max_size

        return removed_item
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = cq.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return self._current_size == 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = cq.is_full()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return self._current_size == self._max_size
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items currently in queue
        Use: num = len(cq)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return self._current_size
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints items in queue in proper order
            prints () if queue is empty
        Use: print(queue) or str(queue)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        -------------------------------------------------------
        """
        if self.is_empty():
            return '()'
        output = ''
        i = self._front
        output = output + str(self._items[i])+' '
        while i != self._rear:
            i = (i-1)%self._max_size
            output = output + str(self._items[i])+' '
        return output

    def print(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints actual contents of cqueue list
            also prints front and rear pointers
        Use: queue.print()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        -------------------------------------------------------
        """
        print('front = {}, back = {}, current_size = {} , contents = \n('.format
              (self._front,self._rear,self._current_size),end='')
        for i in range(self._max_size):
            if i != self._max_size-1:
                print(self._items[i],end=' ')
            else:
                print(self._items[i],end='')
        print(')')
        return
    
class pQueue:
    """
    -------------------------------------------------------
    Implementation of Prioirity Queue ADT (Array-based Implementation)
    unsorted insert approach
    Supports highest value as top priority, or lowest value as top priority
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self,size=DEFAULT_SIZE,mode = 'H'):
        """
        -------------------------------------------------------
        Description:
            Initializes a Priority Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size: maximum size of queue (default = 10)
        Returns:
            A pQueue object (pQueue)            
        -------------------------------------------------------
        """
        assert isinstance(size,int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        self._items = []
        self._size = size
        self._mode = mode
        
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of highest priority item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.peek): Invalid peek operation. Queue is empty')
            return None
        highest = 0
        if self._mode == 'H':
            for i in range(1,len(self._items)):
                if self._items[i] > self._items[highest]:
                    highest = i
        elif self._mode == 'L':
            for i in range(1,len(self._items)):
                if self._items[i] < self._items[highest]:
                    highest = i
        return deepcopy(self._items[highest]) 
    
    def insert(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the priority queue
        Use: queue.insert(item)
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(pQueue.insert): Invalid insert operation. Queue is full')
        else:
            self._items.append(deepcopy(item))
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the item with the highest priority from the queue
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - highest priority item in the queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.remove):Invalid remove operation. Queue is empty')
            return None
        highest = 0
        if self._mode == 'H':
            for i in range(1,len(self._items)):
                if self._items[i] > self._items[highest]:
                    highest = i;
        elif self._mode == 'L':
            for i in range(1,len(self._items)):
                if self._items[i] < self._items[highest]:
                    highest = i;
            
        return deepcopy(self._items.pop(highest))
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = queue.is_empty()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._items)== 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = queue.is_full()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return len(self._items) == self._size
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Override built-in len() method
            Returns number of items currently in queue
        Use: num = len(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return len(self._items)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints all items in Queue in priority order
            (First Second ... Last)
            prints () if queue is empty
        Use: str(queue) 
             print(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if self.is_empty():
            output =  '()'
        else:
            output = '('
            if self._mode == 'H':
                for i in range(len(self._items)-1,-1,-1):
                    output = output + str(self._items[i])+' '
            else:
                for i in range(len(self._items)):
                    output = output + str(self._items[i])+' '
        output = output[:-1]+')'
        return output
