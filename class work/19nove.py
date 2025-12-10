def lcm_num(m,n):
    i=2
    lcm=1
    while m>1 or n>1:
        if m%i==0 or n%i==0:
            if m%i==0:
                m=m//i
            if n%i==0:
                n=n//i
            lcm=lcm*i
        else:
            i+=1
    print(lcm)
lcm_num(3,7)
lcm_num(10,14)
