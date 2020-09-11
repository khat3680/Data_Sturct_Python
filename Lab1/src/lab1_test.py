import Lab1

def t1():
    print('{}'.format('-'*20))
    print('t1: Testing read_airports:\n')
    filename1 = 'airports1.txt'
    dict1,set1 = Lab1.read_airports(filename1)
    print('Airport Dictionary:')
    print(dict1)
    print('Province Set:')
    print(set1)
    print()
    
    filename2 = 'airports2.txt'
    dict2,set2 = Lab1.read_airports(filename2)
    print('Airport Dictionary:')
    print(dict2)
    print('Province Set:')
    print(set2)
    print()
    print('End of t1 testing')
    print('{}\n'.format('-'*20))
    return

def t2():
    print('{}'.format('-'*20))
    print('t2: Testing query_airports_DB:\n')
    code_name_dict = {'YLW': 'Kelowna Airport',
                  'YQB': 'Quebec City Jean Lesage Airport', 
                  'YQG': 'Windsor Airport', 
                  'YVR': 'Vancouver Airport', 
                  'YAD': 'Moose Lake Airport', 
                  'YMX': 'Montreal Mirabel Airport', 
                  'YXE': 'Saskatoon John Diefenbaker Airport', 
                  'YHC': 'Halifax Stanfield Airport', 
                  'YRB': 'Resolute Bay Airport', 
                  'YKF': 'Region of Waterloo Airport'}
    prov_code_dict = {'British Columbia': 'YLW YVR',
                'Quebec' : 'YQB YMX',
                'Ontario': 'YQG YKF',
                'Manitoba': 'YAD',
                'Saskatchewan':'YXE',
                'Nova Scotia':'YHC',
                'Saskatchewan':'YXE',
                'Nova Scotia':'YHC',
                'Nunavut':'YRB'}
    print('code_name_dict = ')
    for item in code_name_dict.items():
        print(item)
    print()
    print('prov_code_dict = ')
    for item in prov_code_dict.items():
        print(item)
    print()
    
    prov_name_dict = Lab1.query_airports_DB(code_name_dict, prov_code_dict)
    print('prov_name_dict:')
    for item in prov_name_dict.items():
        print(item)
    print()
    print('End of t2 testing')
    print('{}\n'.format('-'*20))
    return

def t3():
    print('{}'.format('-'*20))
    print('t3: Testing is_array:\n')
    test_cases = [123,
                  (1,2,3),
                  set([1,2,3]),
                  [1,2.0,3],
                  [[1,2],(3,4),[5,6]],
                  [[1,2],[3,4],[5],[6,7]],
                  [(1,2),(3,4),(5)],
                  [{1},{2,3},{3,4}],
                  [],
                  [[1,2],[3,4],[5,6]],
                  [(1,2),(3,4)],
                  [{1,2},{3,4}]]
    for case in test_cases:
        print('{}? = {}'.format(case,Lab1.is_array(case)))
    print()
    print('End of t3 testing')
    print('{}\n'.format('-'*20))

def t4():
    print('{}'.format('-'*20))
    print('t4: Testing get_num_baskets:\n')
    test_cases = [ 123,
                  [],
                  (1,9,8),
                  (4,16,29,4),
                  (4,5334),
                  [1900,50,18,444,88995,-1],
                  [-55,49,300,-400,8,-6,90000]]
    for case in test_cases:
        print('{} --> {}'.format(case,Lab1.get_num_baskets(case)))
    print()
    print('End of t4 testing')
    print('{}\n'.format('-'*20))

def t5():
    print('{}'.format('-'*20))
    print('t5: Testing is_valid_container:\n')
    test_cases = [ 4, 3.5, [],
                  '[]','()','{}',
                  '[,]','(,)','{,}',
                  '[1]','(2)','{3}',
                  '[1}','(2]','{3)',
                  '[1,]','(2,)','{3,}',
                  '[1,2]','(1,2)','{1,2}',
                  '[1,,2]','(1,2,,3)','{1,2,3,}',
                  '[1,2,3]','(1,2,3)','{1,2,3}']
    counter = 1
    for case in test_cases:
        
        print('{} --> {}'.format(case,Lab1.is_valid_container(case)))
        if counter%3 == 0:
            print()
        counter+=1
    print('End of t5 testing')
    print('{}\n'.format('-'*20))

#uncomment the function you want to test
#t1()
#t2()
#t3()
#t4()
t5()
