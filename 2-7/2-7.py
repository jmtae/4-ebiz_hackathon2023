num=int(input("input숫자를 입력하세요: "))

#초기화 
start =1
count=0

min=float('inf')

while start<num:
    if (num%start==0): # 나눠지면
        count=(num//start)-1  # 1열부터 몇칸인지
       
        count+=start-1  # 1빼고 더해줌
       
        if min>count:
            min=count
        
    start+=1 # 한 칸씩 추가
    
        
print('최소 이동 횟수는:',min)

-----------------------------------------------------
## 주석 설명 버전
# 사용자로부터 숫자를 입력받습니다.
num=int(input("input숫자를 입력하세요: "))

# 필요한 변수를 초기화합니다.
start =1  # start는 약수를 찾기 위한 시작점
count=0   # count는 이동 횟수를 계산하는데 사용

# min은 최소 이동 횟수를 저장하는데 사용되는데 처음에는 99999999 무한대로 설정하기 위해
# 초기값으로 무한대를 설정하여 첫 번째 계산된 이동 횟수가 무조건 min이 되도록 한다.
min=float('inf')

# start가 num보다 작은 동안 반복합니다.
while start<num:
    # num이 start로 나누어 떨어지면, 즉 start가 num의 약수이면
    if (num%start==0):
        # num을 start로 나눈 몫에서 1을 뺀 값을 count에 저장합니다. 이는 1열부터 몇 칸인지를 나타난다.
        count=(num//start)-1  
       
        # count에 start에서 1을 뺀 값을 더하고, 이는 해당 행에서 왼쪽 끝까지의 거리를 나타낸다.
        count+=start-1  
       
        # count가 min보다 작으면 min을 count로 업데이트.
        if min>count:
            min=count
        
    # start를 1 증가시켜 다음 숫자로 넘어간다.
    start+=1 

# 모든 반복이 끝나면 최소 이동 횟수인 min을 출력
print('최소 이동 횟수는:',min)
