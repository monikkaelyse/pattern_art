def train_pattern(num):
    print 'x'
    for i in range(num):
        print 'x',
        for j in range(i):
            print '-',
            if j%2==0:
                print 'x',
        print 'x '
        if i == num-1:
            print 'x ' * (num * 2)
        for l in xrange(num * 2):
            print '-',
            

train_pattern(10)