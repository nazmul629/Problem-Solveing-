for _ in range(int(input())):
    N = input()
   
    if N[0] == '-':
       print('Not a power of 2')
       continue
    
    binary = "{0:b}".format(int(N))

    if binary.count('1') == 1:
        print('It\'s a power of 2' )
    else:
        print('Not a power of 2')
    