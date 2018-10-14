
#Method 1 O(n) complexity
def linearSearch(arr):
    for i in range(len(arr)):
        if(i == 0):
            if(arr[i] > arr[i+1]):
                print (arr[i])

        elif(i == len(arr)):
            if(arr[i-1] < arr[i]):
                print (arr[i])

        else:
            if(i < len(arr) and i+1 < len(arr)):
                if(arr[i] > arr[i+1] and arr[i-1] < arr[i]):
                    print (arr[i])

#Method 2 O(Logn) complexity
def binarySearch(arr, low, high):
    mid = int((low+high)/2)

    if(arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]):
        print(arr[mid])

    if(arr[mid-1] > arr[mid]):
        binarySearch(arr, low, mid-1)

    if(arr[mid] < arr[mid+1]):
        binarySearch(arr, mid+1, high)

arr = [10,20,15,2,23,90,67]

low = 0
high = len(arr)

binarySearch(arr, low, high);
