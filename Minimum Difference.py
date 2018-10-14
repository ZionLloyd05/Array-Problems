
def linear(arr):

    minDif = 1000;

    for i in range(len(arr)):
        for x in range(len(arr)):
            if(i != x):
                if(arr[i]-arr[x] > 0):
                    if((arr[i]-arr[x]) < minDif):
                        minDif = arr[i]-arr[x]
    print(minDif)

# sorting in O(nLogn) complexity
def sort(arr, i):
    x = 0
    if((i+1) < len(arr)):
        if(arr[i] > arr[i+1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            #print("array on ",i," ",arr)
        if((i-1) >= 0):
            if(arr[i-1] > arr[i]):
                x=1
                sort(arr, (i-1))
                #print("array on again",i," ",arr)
        if(i != len(arr)):
            i += 1
            sort(arr, i)
            x=1


#def logarithmic(arr)

arr = [1,19,-4,31,38,25,100]
minDif = 1000;
sort(arr, 0);
linear(arr)
for i in range(len(arr)):
    if(i+1 < len(arr)):
        #print("array on ",i," ",i)
        #print("array on arr[i]"," ",arr[i])
        if(arr[i+1] - arr[i] > 0 and arr[i+1] - arr[i] < minDif):
            minDif = arr[i+1] - arr[i]
print(minDif)
