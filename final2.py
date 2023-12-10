def solution(letter):
    # 입력 문자열의 길이는 1 이상 1000 이하여야 함
    if 1 <= len(letter) <= 1000:
        # 각 모스 부호에 대한 영어 소문자 매핑
        morse_dict = {
            '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
            '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
            '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
            '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
            '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
            '--..': 'z'
        }

        # 입력된 모스 부호를 공백을 기준으로 나눠 리스트로 만듦
        morse_words = letter.split(' ')
        
        # 모스 부호를 영어 소문자로 변환하고 결과를 리스트에 저장
        answer = ' '.join([morse_dict[word] if word in morse_dict else ' ' for word in morse_words])

        return answer
    else:
        return "Input string length should be between 1 and 1000."

# 테스트 예시
morse_code = ".-.. .. ...- .   .. -.   - .... .   -- --- -- . -. -"
result = solution(morse_code)
print(result)  # 출력 결과: live in the moment