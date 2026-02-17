a=[1,10,2]
for i in range(len(a)):
    print(a[i])
    for j in range(i+1,len(a)):
        print(a[i],a[j])



#power_set with recursion
def powerset(arr,index=0,current=[]):
    if index==len(arr):
        print(current)
        return
    powerset(arr,index+1,current)
    powerset(arr,index+1,current+[arr[index]])
arr=[1,2,3]
powerset(arr)    
