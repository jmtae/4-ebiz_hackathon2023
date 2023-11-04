def count_chars_in_spanish(input_spanish):
    allowed_input = "abcdefghijklmnopqrstuvwxyz,~."
    
    # 입력 문자열을 소문자로 변환( 대문자가 입력 되어도 소문자로 변환하도록 하였다.)
    input_spanish = input_spanish.lower()
    
    # 제한된 문자 범위를 벗어나는 문자가 있는지 확인
    if any(char not in allowed_input for char in input_spanish):
        print("제한된 문자 범위를 벗어나는 문자가 포함되어 있습니다. 다시 입력하세요.")
        return None
    
    # 확장문자를 하나로 체크하도록
    replacements = {
        "a,": "a",
        "e,": "e",
        "i,": "i",
        "n~": "n",
        "o,": "o",
        "u,": "u",
        "u,,": "u"
    }
    
    for key, value in replacements.items():
        input_spanish = input_spanish.replace(key, value)
    
    count = sum(1 for char in input_spanish if char in allowed_input if char.isalpha())
    
    return input_spanish, count

# 스페인어 입력
spanish_input = input("스페인어를 입력하세요: ")

# 사용자가 올바른 문자열을 입력할 때까지 반복
while True:
    result = count_chars_in_spanish(spanish_input)
    if result is not None:
        transformed_spanish_input, char_count = result
        print(f"스페인 알파벳 개수는 {char_count}개 입니다.")
        break
    spanish_input = input("다시 입력하세요: ")
