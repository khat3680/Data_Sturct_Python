from data import Process
from data_structures import Stack, Queue
from midterm import stacks_to_queues, MapList, schedule_RR


def test_stacks_to_queues():
    print('{}'.format('-' * 20))
    print('Start of Task 1 Testing (stacks_to_queues):\n')
    
    cases = [[1, 2, 3], [], [10, 20], [100, 200, 300, 400]]
    sizes = [3, 1, 2, 4]
    master_stack1 = Stack(len(cases))
    for i in range(len(cases) - 1, -1, -1):
        stack = Stack(sizes[i])
        for item in cases[i]:
            stack.push(item)
        master_stack1.push(stack)

    print('master_stack before calling function:')
    print(master_stack1)
    print()
    
    print('master_queue1 after calling function:')
    master_queue1 = stacks_to_queues(master_stack1)
    print(master_queue1)
    print()
    
    print('Verity that master_stack1 is empty after calling function:')
    print(master_stack1)
    
    print()
    print('Verifying Sizes:')
    counter = 0
    while not master_queue1.is_empty():
        print('Queue {} size = {}'.format(counter, master_queue1.remove()._size))
        counter += 1
    print()
    
    master_queue2 = stacks_to_queues(Stack(5))
    print('Contents of master_queue if master_stack is empty: {}'.format(master_queue2))
    print('Size of master_queue2 = {}'.format(master_queue2._size))
    print()
    
    master_queue3 = stacks_to_queues(Queue(5))
    print('Contents of master_queue if master_stack is invalid: {}'.format(master_queue3))
    print('Size of master_queue3 = {}'.format(master_queue2._size))
    print()
    
    print('End of Task 1 testing')
    print('{}\n'.format('-' * 20))
    return


def test_MapList():
    print('{}'.format('-' * 20))
    print('Start of Task 2 Testing (MapList):\n')
    
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    days = [[1, 'Sunday'], (2, 'Monday'), [3, 'Tuesday'], (4, 'Tuesday'), 5, 'Thursday']
    nums = [i for i in range(1, 13)]

    print('Creating months MapList (map1):')
    map1 = MapList(nums, months)
    print(map1)
    
    print('length = {}'.format(len(map1)))
    print('is_empty? = {}'.format(map1.is_empty()))
    print()
    
    print('get(3) = {}'.format(map1.get(3)))
    print('get(13) = {}'.format(map1.get(13)))
    print()
    
    print('4 in map1? = {}'.format(4 in map1))
    print('14 in map1? = {}'.format(14 in map1))
    print()
    
    print('index(7) = {}'.format(map1.index(7)))
    print('index(-3) = {}'.format(map1.index(-3)))
    print()
    
    print('remove(3):')
    print('removed item = {}'.format(map1.remove(3)))
    print('list afer remove =')
    print(map1)
    print()
    
    print('remove(15):')
    print('removed item = {}'.format(map1.remove(15)))
    print('list afer remove =')
    print(map1)
    print()

    print()
    
    print('Creating empty MapList (map2):')
    map2 = MapList()
    print(map2)
    print('length = {}'.format(len(map2)))
    print('is_empty? = {}'.format(map2.is_empty()))
    print()
    
    print('insert several items to map2')
    for day in days:
        map2.insert(day)
    print('list after insert:')
    print(map2)
    print()
    
    print('Comparing map1 and map2:')
    print('map1 == map2? = {}'.format(map1 == map2))
    print('map1 != map2? = {}'.format(map1 != map2))
    print('map1 > map2? = {}'.format(map1 > map2))
    print('map1 >= map2? = {}'.format(map1 >= map2))
    print('map1 < map2? = {}'.format(map1 < map2))
    print('map1 <= map2? = {}'.format(map1 <= map2))
    print()
    
    print('list version of map1:')
    print(map1.to_list())
    print('list version of map2:')
    print(map2.to_list())
    print()
    
    print('Get dictionary version of map1:')
    dict1 = map1.to_dict()
    print('Verify that output is of type dict1 = {}'.format(isinstance(dict1, dict)))
    print('dict1[6] = {}'.format(dict1[6]))
    print()
    
    print('Clear both maps:')
    map1.clear()
    map2.clear()
    print('map1 = {}'.format(map1))
    print('map2 = {}'.format(map2))
    print()
    
    print('End of Task 2 testing')
    print('{}\n'.format('-' * 20))
    return


def test_RR():
    print('{}'.format('-' * 20))
    print('Start of Task 3 (Round Robin Scheduler):\n')
    
    processes = read_processes('processes1.txt')
    schedule_RR(processes, 8)
    print()
    
    processes = read_processes('processes1.txt')
    schedule_RR(processes, 3)
    print()
 
    print('End of Task 3 testing')
    print('{}\n'.format('-' * 20))
    return


def read_processes(filename):
    processes = []
    in_file = open(filename, 'r')
    for line in in_file:
        line = line[1:-2]  # get rid of '[' and ')\n'
        arrival, rest = line.split(']')
        PID, time = rest.split(',')
        PID = int(PID[1:])  # PID is always 10 digits
        process = Process(PID, int(time), int(arrival))
        processes.append(process)
    in_file.close()
    return processes


# test_stacks_to_queues()
# test_MapList()
test_RR()   
