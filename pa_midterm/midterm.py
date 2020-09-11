"""
-------------------------
# Student Name: Pranav Verma
# Student ID:193272030
# Student email:verm2030@mylaurier.ca
#-------------------------
"""
"""
#-------------------------
Put the Academic honesty Certification here
“I certify that I completed this midterm according to academic honesty guidelines. 
I attest that I did not use any external help, neither in person nor virtually. I 
understand that plagiarizing will lead to my failure in the course, in addition to 
other penalties according to the University policies”.  
#-------------------------
"""
"""
#-------------------------
If you have any comments to the instructor put it here

#-------------------------
"""
"""------------ Task 1 -------------"""

from copy import deepcopy

from data_structures import Stack, Queue, pQueue


def stacks_to_queues(master_stack):
    list = []
    if master_stack.is_empty():
        if not isinstance(master_stack, Stack):
            print("Error(stacks_to_queues): invalid input")
        master_queue = Queue(10)
    
    else:
        while not master_stack.is_empty():
            p = master_stack.pop()
            q = []
            while not p.is_empty():
                q.append(p.pop())
            list.append(q)
        master_queue = Queue(len(list))
        for i in range(len(list)):
            if len(list[i]) == 0:
                size = 10
            else: 
                size = len(list[i])
            temp_queue = Queue(size)
            for j in list[i]:
                temp_queue.insert(j)
            master_queue.insert(temp_queue)
    return master_queue


"""------------ Task 2 -------------"""


class MapList:
 
    def __init__(self, key=[], values=[]):
        self._key = key
        self._values = values
         
    def is_empty(self):
        return len(self._key) == 0 and len(self._values) == 0
 
    def insert(self, key, value):
        if self.is_empty:
            self._key.insert(0, deepcopy(key)) and self._value.insert(0, deepcopy(value))
        else:
            self._key.append(deepcopy(key)) and self._value.append(deepcopy(value))
        return
      
    def remove(self, key, value):   
        if not self._key:
            print("Error(MapList.get): key not found")
            return None
        else:
            a = set()
            x = deepcopy(self._key.pop(key))
            y = deepcopy(self._value.pop(value))
            a.add(x, y)
            return a
 
    def index(self, key):
        for i in self._key:
            if i not in self._key:
                return -1
        else:
            return(self._key.index[i])

    def __eq__(self, other):
        return self._key == other._key and self._values == other._values 

    def __ne__(self, other):
        return not self == other
    
    def __gt__(self, other):
        if self._key > other._key:
            return True
        if self._key < other._key:
            return False
        
        if self._values > other._values:
            return True
        
        return False
    
    def __ge__(self, other):
        return self == other or self > other
    
    def __lt__(self, other):
        if self._key < other._key:
            return True
        if self._key > other._key:
            return False
        
        if self._values < other._values:
            return True
        
        return False
    
    def __le__(self, other):
        return self == other or self < other
        
    def clear(self):     
        del self._keys[:]  
        del self._values[:]
        """------------ Task 3 -------------"""


def schedule_RR(processes, interval):
    timer = 0
    counter = 0
    queue = pQueue(21, 'L')

    for i in range(len(processes) - 1, -1, -1):
        queue.insert(processes[i])
    process = queue.peek()

    while not queue.is_empty():
        process = queue.peek()
        if counter < process.arrival:
            if timer == 0:
                print('[Timer:{}]: Starting RR(8) Scheduler'.format(timer))
            else:
                print('[Timer:{}]: idle'.format(counter))
            counter += 1
            timer += 1
        else:
            process = queue.remove()
            if queue.is_empty():
                print('Fetching Process: {}'.format(process))
                for i in range(process.time % interval):
                    print('[Timer:{}]: {}'.format(counter, process.PID))
                    counter += 1
                    if next is not None:
                        if timer > next.arrival:
                            timer += 1
            else:
                next = queue.peek()
                print('Fetching Process: {}'.format(process))
                for i in range(process.time % interval):
                    print('[Timer:{}]: {}'.format(counter, process.PID))
                    counter += 1
                    if next is not None:
                        if timer > next.arrival:
                            timer += 1
    print('[Timer:{}]:  Closing RR Scheduler'.format(counter))
    return
    
