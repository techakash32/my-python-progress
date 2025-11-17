for i in range(1,5):
    for j in range(1,1+i):
        print(" ",end="")

    for k in range( 1,6-i):
        if( k==1 or i==1 or i+k==4-i):
           
            print( "*",end=" ")
        else:
            print(" ",end=" ")    

    print(" ")
