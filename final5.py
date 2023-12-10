def solution(numbers):
    # 정렬 기준 설정
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 1000이하의 수이므로 3자리로 맞춰 비교
    
    # 만들어진 가장 큰 수 조합
    answer = str(int(''.join(numbers)))  # 앞에 나올 수 있는 0을 제거하기 위해 int로 변환 후 다시 str로 변환
    
    return answer

# 테스트
numbers = [8, 30, 17, 2, 23]
result = solution(numbers)
print(result)