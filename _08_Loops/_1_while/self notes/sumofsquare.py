#SUM OF SQUARE NUMBER
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID INPUT")
else:
    i=1
    s=0
    while(i<=n):
        s=s+i**2
        print(i**2)
        i=i+1
    else:
        print("sum of {} is ".format(s))
