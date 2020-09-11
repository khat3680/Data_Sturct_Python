"""
-------------------------
# Student Name: Pranav verma
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

#-------------------------
from copy import deepcopy

from data_structures import Stack, Queue, pQueue

#-------------------------

"""------------ Task 1 -------------"""


def stacks_to_queues(master_stack):
    list1 = []
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
            list1.append(q)
        master_queue = Queue(len(list1))
        for i in range(len(list1)):
            if len(list1[i]) == 0:
                size = 10
            else: 
                size = len(list1[i])
            temp_queue = Queue(size)
            for j in list1[i]:
                temp_queue.insert(j)
            master_queue.insert(temp_queue)
    return master_queue


"""------------ Task 2 -------------"""


class MapList:

    def __init__(self, keys=None, values=None):  # <----- edit this
        self._items = []
        if keys is not None and values is not None:
            i = 0
            for key in keys:
                self._items.append([key, values[i]])
                i += 1
                
    def is_empty(self):
        empty = False
        if len(self._items) == 0:
            empty = True
        return empty
    
    def insert(self, item):
        if isinstance(item, list):
            self._items.append(item)
        elif isinstance(item, tuple):
            self._items.append([item[0], item[1]])
        else:
            print("Error(MapList.insert): invalid input")
        return
    
    def __len__(self):
        return len(self._items)

    def remove(self, key):
        i = 0
        output = None
        while i < len(self._items) and self._items[i][0] != key:
            i += 1
        if i == len(self._items):
            print("Error(MapList.remove): key not found")
        else: 
            output = tuple(self._items.pop(i))
        return output
    
    def index(self, key):
        i = 0
        output = -1 
        while i < len(self._items) and self._items[i][0] != key:
            i += 1
        if i == len(self._items):
            print("Error(MapList.index): key not found")
        else: 
            output = i
        return output   
       
    def get(self, key):
        i = 0
        output = None 
        while i < len(self._items) and self._items[i][0] != key:
            i += 1
        if i == len(self._items):
            print("Error(MapList.get): key not found")
        else: 
            output = deepcopy(self._items[i][1])
        return output      

    def to_list(self):
        list1 = deepcopy(self._items)
        return list1
    
    def to_dict(self):
        dict1 = {}
        for item in self._items:
            dict1[item[0]] = item[1]
        return dict1
    
    def clear(self):
        self._items = []
        
    def __str__(self):
        output = "["
        for item in self._items:
            output += "{}-->{},".format(item[0], item[1])
        if len(output) > 1:
            output = output[:-1] + "]"
        else:
            output = output + "]"
        return output

    def __eq__(self, other):
        equal = False
        if len(self._items) == len(other._items):
            equal = True
        return equal
    
    def __ne__(self, other):
        return not self == other
    
    def __gt__(self, other):
        gt = False
        if len(self._items) > len(other._items):
            gt = True
        return gt
    
    def __ge__(self, other):
        ge = False
        if len(self._items) >= len(other._items):
            ge = True
        return ge

    def __lt__(self, other):
        lt = False
        if len(self._items) < len(other._items):
            lt = True
        return lt
    
    def __le__(self, other):
        le = False
        if len(self._items) <= len(other._items):
            le = True
        return le

    def __iter__(self):
        for i in self._items:
            yield i[0]


"""------------ Task 3 -------------"""


def schedule_RR(processes, interval):

    timer = 0
    counter = 0
    queue = pQueue(len(processes), 'L')
 
    for i in range(len(processes) - 1, -1, -1):
        queue.insert(processes[i])
    process = queue.peek()
 
    while not queue.is_empty():
        process = queue.peek()
        if counter < process.arrival:
            if timer == 0:
                print('[Timer:{}]: Starting RR({}) Scheduler'.format(timer, interval))
            else:
                print('[Timer:{}]: idle'.format(counter))
            counter += 1
            timer += 1
                
        else:
            process = queue.remove()
            if queue.is_empty():
                print('Fetching Process: {}'.format(process))
                for i in range(process.time):
                    print('[Timer:{}]: {}'.format(counter, process.PID))
                    counter += 1
                    if timer == process.arrival - interval:
                        continue
                        timer = timer + 3
                        counter -= interval
                        
                        if next is not None:
                            if timer > next.arrival:
                                timer += 1
                            
            else:
                next = queue.peek()
                print('Fetching Process: {}'.format(process))
                for i in range(process.time):
                    print('[Timer:{}]: {}'.format(counter, process.PID))
                    counter += 1
                    if timer == process.arrival + interval:
                        continue
                        timer = timer + 3
                        counter -= interval
                        if next is not None:
                            if timer > next.arrival:
                                timer += 1
    print('[Timer:{}]:  Closing RR Scheduler'.format(counter))
    return
     

     
