# 사용자로부터 n 값 입력 받음 (2에서 50까지만 허용)
while True:
    n = int(input("매트릭스의 크기 N을 입력하세요 (2에서 50 사이): "))
    if 2 <= n <= 50:
        break
    else:
        print("2에서 50 사이의 값을 입력하세요.")

# NxN 크기의 매트릭스를 생성하고 각 요소에 0에서 9 사이의 값 입력
matrix = []

for i in range(n):
    while True:
        row_input = input(f"{i + 1}번째 행의 {n}개의 숫자를 공백으로 구분하여 입력하세요 (0에서 9까지의 값만 허용): ").split()[:n]
        if len(row_input) == n and all(0 <= int(x) <= 9 for x in row_input):
            row = list(map(int, row_input))
            break
        else:
            print("0에서 9 사이의 값을 정확하게 입력하세요. 이 행을 다시 시작합니다.")

    matrix.append(row)

# 각 행에서의 최댓값을 저장하는 리스트를 생성
max_in_rows = [max(row) for row in matrix]

# 각 열에서의 최댓값을 저장하는 리스트를 생성
max_in_columns = [max(column) for column in zip(*matrix)]

# 첫 번째 행과 첫 번째 열의 값이 각 행과 열의 최댓값 중 최솟값을 저장하는 매트릭스 생성
new_matrix = [[min(max_in_rows[i], max_in_columns[j]) for j in range(n)] for i in range(n)]

# 새로운 매트릭스에서 원래 매트릭스를 빼고 총 합 계산
total_difference = sum(new_matrix[i][j] - matrix[i][j] for i in range(n) for j in range(n))

# 생성된 매트릭스와 새로운 매트릭스 출력
print("원래 매트릭스:")
for row in matrix:
    print(row)
print("새로운 매트릭스:")
for row in new_matrix:
    print(row)

# 총 합 출력
print("새로운 매트릭스에서 원래 매트릭스를 빼고 도시의 처음 모습을 유지하면서 사용할 수 있는 레고 블록 개수의 총합은:", total_difference)
