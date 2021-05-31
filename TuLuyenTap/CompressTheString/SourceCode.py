a=input()
s=''
for i in range(len(a)):
    
    if i!=0:
        if a[i]==a[i-1]:
            continue
    tmp=0
    for j in range(i,len(a)):
        if  a[j]==a[i]:
            tmp+=1
        else:
            break
    print('('+str(tmp)+', '+str(a[i])+')',end=' ')
    