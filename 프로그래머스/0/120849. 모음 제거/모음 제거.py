def solution(my_string):
    answer = ''.join([s for s in my_string if s not in ['a','e','i','o','u']])
    return answer