if __name__ == "__main__":
    length = int(input("Enter the number: "))
    row = col = (length*2)-1

    for i in range(row):
        if i==0 or i==(col-1):
            for j in range(col):
                print(length, end="")
        elif i<length:
            for j in range(i):
                print(length-j, end="")
            for j in range(i, col-i):
                print(length-i, end="")
            for j in range(col-i, col):
                print(length-(col-j-1), end="")
        else:
            k = col-1-i
            for j in range(k):
                print(length-j, end="")
            for j in range(k, col-k):
                print(length-k, end="")
            for j in range(col-k, col):
                print(length-(col-j-1), end="")
        print()
