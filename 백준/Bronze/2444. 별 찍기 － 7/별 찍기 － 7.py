def print_pyramid(n: int): #n을 입력받아서 커지는 함수
    # TODO: implement this function
    for i in range(1,n+1):
        print(' '*(n-i) + '*'*(2*i-1))


def print_inverted_pyramid(n: int):
    for i in range(1,n):
        print(" "*i + "*"*(2*(n-i)-1))


if __name__ == "__main__":
    N = int(input())
    print_pyramid(N)
    print_inverted_pyramid(N)