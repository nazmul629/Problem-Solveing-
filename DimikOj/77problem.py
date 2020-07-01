for i in range(int(input())):

    def function(*num):

        sum = 0;
        for j in num[1:]:
            sum +=j;
    
        if sum % 4 == 0:
            print('yes')
        else:
            print('no')
            
    mylist = [int(n) for n in input().split()]
    function(mylist) 