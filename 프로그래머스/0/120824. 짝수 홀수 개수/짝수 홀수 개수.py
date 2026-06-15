def solution(num_list):
    odd = [i for i in num_list if i&1]
    answer = [len(num_list)-len(odd), len(odd)]
    return answer