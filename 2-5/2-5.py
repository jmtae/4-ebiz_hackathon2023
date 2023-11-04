#1번
n = 4  # 역 피라미드의 높이를 설정합니다.

for i in range(n, 0, -1):
    # 공백을 출력합니다.
    for j in range(n - i):
        print(" ", end="")
    
    # 별표를 출력합니다.
    for k in range(2 * i - 1):
        print("*", end="")
    
    # 줄 바꿈을 추가합니다.
    print()

#2번
n = 8  # 모래시계의 높이

# 모래시계 상단 부분 
for i in range(n, 0, -2):
    row = " " * ((n - i) // 2) + "*" * i
    print(row)

# 모래시계 하단 부분 
for i in range(2, n + 1, 2):
    row = " " * ((n - i) // 2) + "*" * i
    print(row)

# 3번
width = 10  # 가로 길이 설정
height = 9 # 세로 길이 설정
for i in range(1, 10, 2):  # 세로 길이가 홀수인 경우만 반복
    if i == 1 or i == height:
        print("*" * width)
    else:
        spaces = " " * (width - 2)
        row = "*" + spaces + "*"
        print(row)
