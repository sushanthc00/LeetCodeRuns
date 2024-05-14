def squareStars(N):
    for i in range(0, N):
        for j in range(0, N):
            print("*", end="")
        print()


if __name__ == '__main__':
    N = int(input("Numbers of lines you need in your block: "))
    squareStars(N)
