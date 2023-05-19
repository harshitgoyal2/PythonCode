if __name__ == "__main__":
    number = int(input("Enter the number: "))
    for i in range(number):
        if i == 0  or i == number-1:
            for j in range(number):
                print(number, end=" ")
        else:
            for j in range(number):
                if j == 0 or j == number-1:
                    print(number, end=" ")
                else:
                    print(end="  ")
        print("\n")
