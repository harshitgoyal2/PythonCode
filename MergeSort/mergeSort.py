def printArr(arr):
    for num in arr:
        print(num, end=" ")
    print()

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        i=j=k=0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                arr[k] = leftArr[i]
                i+=1
            else:
                arr[k] = rightArr[j]
                j+=1
            k+=1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i+=1
            k+=1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j+=1
            k+=1
    else:
        return

if __name__ == "__main__":
    length = int(input("Enter the length of the array: "))
    arr = [0]*length
    for i in range(length):
        ele = int(input())
        arr[i]=ele
    print("Array before merge sort: ", end="")
    printArr(arr)
    mergeSort(arr)
    print("Array after merge sort: ", end="")
    printArr(arr)
