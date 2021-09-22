n = int(input())
pos = int(input())
m = int(input())
arr = list(map(int,input().split()))
tmp1,tmp2 = m,m

def forBac(i,arr):
    n = len(arr)
    v1 = sum(arr[i:i+m])
    v2 = sum(arr[i-m+1:i+1])
    tmp = max(v1,v2)
    return tmp

maxi1 = -99999
maxi2 = -99999

i = pos
while(tmp1>0):
    maxi1 = max(maxi1,forBac(i,arr))
    i+=1
    tmp1-=1

i = pos
while(tmp2>0):
    maxi2 = max(maxi2,forBac(i,arr)) 
    i+=1
    tmp2-=1

print(max(maxi1,maxi2))

