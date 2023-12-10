def solution(my_string, target):
    # 초기값 설정
    answer = 0

    # 주어진 제한사항에 따라 조건 확인
    if 1 <= len(my_string) <= 100 and my_string.islower() and 1 <= len(target) <= 100 and target.islower():
        # target이 my_string의 부분 문자열인지 확인
        if target in my_string:
            # 부분 문자열이면 answer를 1로 설정
            answer = 1

    return answer

# 테스트
my_str = "abcdef"
my_target = "cde"

result = solution(my_str, my_target)
print(result)
