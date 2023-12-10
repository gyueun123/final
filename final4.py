def solution(r1, r2):
    # r2가 r1보다 커야 하는 조건 확인
    if r2 <= r1:
        return 0  # 조건을 만족하지 않으면 0을 반환

    # 정수 좌표를 가진 점의 개수를 0으로 초기화
    answer = 0

    # x좌표에 대한 반복문
    for x in range(-r2, r2 + 1):
        # y좌표에 대한 반복문
        for y in range(-r2, r2 + 1):
            # 현재 좌표 (x, y)에서의 거리를 계산
            distance_squared = x**2 + y**2
           
            # 현재 좌표가 두 원 내부에 속하는지 확인
            if distance_squared >= r1**2 and distance_squared <= r2**2:
                # 속한다면 정수 좌표를 가진 점의 개수 증가
                answer += 1

    # 최종 결과 반환
    return answer

# r1, r2 각각 3, 5 입력
result = solution(3, 5)
print(result)