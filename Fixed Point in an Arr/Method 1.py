
#Method 1 O(n) Complexity for worst case
def linearSearch(arr):
    for i in range(len(arr)):
        if(i == arr[i]):
            print (i)

#Method 2, Binary Search O(1) Complexity 
def binarySearch(arr, low, high):

    if(high >= low):
        mid = int(((high+low)/2))
        if(mid == arr[mid]):
            print (mid)
        elif(mid > arr[mid]):
            binarySearch(arr, mid+1, high)
        else:
            binarySearch(arr, low, mid-1)


arr = [-10,-5,2,4,6,7]

binarySearch(arr, 0, len(arr)-1)
