with open('sample2.txt', 'w') as tables:
    for i in range(1, 13):
        for j in range(1, 13):
            print('{1:>2} times {0} = {2}'.format(i, j, i * j), file=tables)
        print('=' * 20, file=tables)
    