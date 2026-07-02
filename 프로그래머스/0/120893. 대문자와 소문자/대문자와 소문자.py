def solution(my_string):
    answer = ''
    for char in my_string:
        if ord(char) >= 65 and ord(char) <= 90:
            answer += chr(ord(char)+32)
        elif ord(char) >= 97 and ord(char) <= 122:
            answer += chr(ord(char)-32)
    return answer