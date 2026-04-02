add_part_list = input().split('-')
result = sum(map(int, add_part_list[0].split('+')))
for add_part in add_part_list[1:]:
    result -= sum(map(int, add_part.split('+')))
print(result)