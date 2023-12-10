def solution():
    alphabet_mapping = {
        'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4',
        'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'
    }

    # 알파벳 입력 받기 (소문자로 변환)
    age_input = input("알파벳을 입력하세요: ").lower()

    # 입력된 알파벳을 PROGEAMMER-857 식 나이로 변환
    answer = ''
    for char in age_input:
      # 알파벳에 해당하는 값으로 변환
      answer += alphabet_mapping[char]
    
    # 변환된 값이 1000을 넘긴 경우, 에러 메시지 출력  
    if int(answer) > 1000:
        return "Error: 변환된 값이 범위 이상입니다."

    return answer

# 함수 호출
result = solution()
print("PROGEAMMER-857 식 나이:", result)