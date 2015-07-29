def triangle_pattern(num):
    ''' Makes pattern in shape:

    x
    x x 
    x - x 
    x - - x 
    x - - - x 
    x - - - - x 
    x - - - - - x 
    x - - - - - - x 
    x - - - - - - - x 
    x - - - - - - - - x 
    x - - - - - - - - - x 
    x x x x x x x x x x x x
    
    '''
    print 'x'
    for i in range(num):
        print 'x',
        for j in range(i):
            print '-',
        print 'x '
        if i == num-1:
            print 'x ' * (num + 2)
