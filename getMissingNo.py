
def getMissing(arr, n):

    total = (n+1)*(n+2)/2

    for i in range(len(arr)):
        total -= arr[i]

    print (total)

arr = [1,2,3,5,6]
getMissing(arr, len(arr))
