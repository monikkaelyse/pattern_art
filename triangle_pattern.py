def triangle_pattern(num):
    print 'x'
    for i in range(num):
        print 'x',
        for j in range(i):
    #         print j
            print '-',
        print 'x '
        if i == num-1:
            print 'x ' * (num + 2)
