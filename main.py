if __name__ == '__main__':
    reference= []
    balance = {}
    price=5
    buy=[]
    print('Product List')
    print('product 1 --->  5$ Price')
    while True:
        print('\n')
        name= input('whats your name:')
        ref_num = int(input('How many people u want to refer:'))
        data = []
        for i  in range(0,ref_num):
            temp = input('Name Of the Reference: ')
            reference.append(temp)
        prd = int(input('How many product u want to buy:'))
        print('Total You will get: Total {} Items '.format(prd+ref_num+int(ref_num/2) ))
        print('congratulations! you get {} free meal for your referal'.format(ref_num+int(ref_num/2)))
        flag = input('Press Enter to buy again|| and press 0 to exit!!!')
        if flag=='0':
            break
