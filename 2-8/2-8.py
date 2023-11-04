# 사용자로부터 매트릭스의 크기 N을 입력받습니다.
N = int(input("매트릭스의 크기 N을 입력하세요: "))

# NxN 크기의 매트릭스를 생성합니다.
matrix = []

# 각 행의 값을 사용자로부터 입력받습니다.
for i in range(N):
    print(f"{i+1}번째 행의 {N}개의 숫자를 공백으로 구분하여 입력하세요:")
    row = list(map(int, input().split()))
    matrix.append(row)

# 각 행에서의 최댓값을 저장하는 리스트를 생성합니다.
max_in_rows = [max(row) for row in matrix]

# 각 열에서의 최댓값을 저장하는 리스트를 생성합니다.
max_in_columns = [max(column) for column in zip(*matrix)]

# 첫 번째 행과 첫 번째 열의 값이 각 행과 열의 최댓값 중 최솟값을 저장하는 매트릭스를 생성합니다.
new_matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        new_matrix[i][j] = min(max_in_rows[i], max_in_columns[j])

# 새로운 매트릭스에서 원래 매트릭스를 빼고 총 합을 계산합니다.
total_difference = 0
for i in range(N):
    for j in range(N):
        difference = new_matrix[i][j] - matrix[i][j]
        total_difference += difference

# 생성된 매트릭스와 새로운 매트릭스를 출력합니다.
print("원래 매트릭스:")
for row in matrix:
    print(row)
print("새로운 매트릭스:")
for row in new_matrix:
    print(row)

# 총 합을 출력합니다.
print("총 합:", total_difference)
