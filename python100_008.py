#99乘法表#
for i in range(1,10):
    for j in range(1,10):
            if i<=j:
                string = '%d*%d=%d'%(i,j,i*j)
                print(string,end='\t')
    print('\n')
