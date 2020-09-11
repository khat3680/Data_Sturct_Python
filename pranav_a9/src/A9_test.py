from bst import BST


def get_bst():
    bst = BST()
    cases = [25, 13, 11, 35, 19, 18, 20, 33, 40, 30, 9, 12, 34, 38, 44, 32]
    for case in cases:
        bst.insert(case)
    return bst


def test_equal():
    print('{}'.format('-' * 20))
    print('Testing BST equal operator:\n')
    
    bst1 = BST()
    bst2 = BST()
    print('bst1 = {}'.format(bst1.inorder()))
    print('bst2 = {}'.format(bst2.inorder()))
    print('bst1 == bst2? {}'.format(bst1 == bst2))
    print()
    
    bst1.insert(25)
    bst1.insert(30)
    bst2.insert(25)
    bst2.insert(30)
    bst2.insert(40)
    print('bst1 = {}'.format(bst1.inorder()))
    print('bst2 = {}'.format(bst2.inorder()))
    print('bst1 == bst2? {}'.format(bst1 == bst2))
    print()
    
    bst1 = get_bst()
    bst2 = get_bst()
    print('bst1 = {}'.format(bst1.inorder()))
    print('bst2 = {}'.format(bst2.inorder()))
    print('bst1 == bst2? {}'.format(bst1 == bst2))
    print()
    
    bst2.remove(32)
    print('bst1 = {}'.format(bst1.inorder()))
    print('bst2 = {}'.format(bst2.inorder()))
    print('bst1 == bst2? {}'.format(bst1 == bst2))
    print()
    
    bst1.remove(20)
    print('bst1 = {}'.format(bst1.inorder()))
    print('bst2 = {}'.format(bst2.inorder()))
    print('bst1 == bst2? {}'.format(bst1 == bst2))
    print()
    
    print('End of BST equality operator testing testing')
    print('{}\n'.format('-' * 20))
    return


def test_valid():
    print('{}'.format('-' * 20))
    print('Testing BST.valid:\n')
    
    bst = BST()
    print('bst = {}'.format(bst.inorder()))
    print('bst.valid() = {}'.format(bst.is_valid()))
    print()
    
    bst = get_bst()
    print('bst = {}'.format(bst.inorder()))
    print('bst.valid() = {}'.format(bst.is_valid()))
    print()
    
    print('change bst property (change 19 to 29):')
    bst._root._left._right._data = 29
    print('bst = {}'.format(bst.inorder()))
    print('bst.valid() = {}'.format(bst.is_valid()))
    print()
    
    print('change bst property (change 38 to 48):')
    bst._root._left._right._data = 19
    bst._root._right._right._left._data = 48
    print('bst = {}'.format(bst.inorder()))
    print('bst.valid() = {}'.format(bst.is_valid()))
    print()
    
    print('End of BST.valid testing')
    print('{}\n'.format('-' * 20))
    return


def test_reflect():
    print('{}'.format('-' * 20))
    print('Testing BST.reflect_vertical:\n')
    print('Note: printing using inorder')
    
    bst = BST()
    print('bst1 = {}'.format(bst.inorder()))
    bst2 = bst.reflect_vertical()
    print('bst2 = {}'.format(bst2.inorder()))
    print()
    
    cases = [25, 13, 35, 11, 40, 19, 20, 18]
    for case in cases:
        bst.insert(case)
        print('bst1 = {}'.format(bst.inorder()))
        bst2 = bst.reflect_vertical()
        print('bst2 = {}'.format(bst2.inorder()))
        print()
    
    print('End of BST.reflect vertical testing')
    print('{}\n'.format('-' * 20))
    return


def test_property1():
    print('{}'.format('-' * 20))
    print('Testing BST.property1:\n')
    
    bst = BST()
    print('bst = {}'.format(bst.inorder()))
    print('Satisfy Property 1? = {}'.format(bst.satisfy_property1()))
    print()
    
    cases = [25, 13, 11, 19, 35, 20, 40, 33]
    for case in cases:
        bst.insert(case)
        print('bst = {}'.format(bst.inorder()))
        print('Satisfy Property 1? = {}'.format(bst.satisfy_property1()))
        print()
    
    print('End of BST.property1 testing')
    print('{}\n'.format('-' * 20))
    return


def test_property2():
    print('{}'.format('-' * 20))
    print('Testing BST.property2:\n')
    
    bst = BST()
    print('bst = {}'.format(bst.inorder()))
    print('Satisfy Property 2? = {}'.format(bst.satisfy_property2()))
    print()
    
    cases = [25, 13, 11, 19, 35, 20, 40, 33, 18]
    for case in cases:
        bst.insert(case)
        print('bst = {}'.format(bst.inorder()))
        print('Satisfy Property 2? = {}'.format(bst.satisfy_property2()))
        print()
    
    print('End of BST.property2 testing')
    print('{}\n'.format('-' * 20))
    return


test_equal()
test_valid()
# test_reflect()
# test_property1()
# test_property2()
