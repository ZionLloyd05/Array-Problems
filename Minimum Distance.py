
def linear(arr, x, y):

    minDistance = 1000
    
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            z = j+1
            if(z < len(arr)):
                if((x == arr[i] and y == arr[z]) or (y == arr[i] and x == arr[z]) and (int(i-z < minDistance))):
                    #print("i ", i)
                    #print("j ", j)
                    minDistance = int(i-z)
    print(minDistance)


def findMinDist(arr, x, y):
    prev = 0;
    minDist = 1000;

    for i in range(len(arr)):
        if(arr[i] == x or arr[i] == y):
            prev = i
            break

    for i in range(len(arr)):
        if(arr[i] == x or arr[i] == y):
            if(arr[i] != arr[prev] and (i - prev) < minDist):
                minDist = i - prev
                prev = i
            else:
                prev = i
    print(minDist)
    

arr = [3,5,4,6,5,5,3,4,3]
linear(arr, 3, 6)
findMinDist(arr, 3, 6)
