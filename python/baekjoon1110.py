N= int(input())
F=N
count=0
while True:
    D=(F//10)
    E=(F%10)
    
    
    NEW1=(D+E)%10
    F=(E*10)+NEW1
    
    count=count+1
    
    if(F==N):
        break
    
print(count)