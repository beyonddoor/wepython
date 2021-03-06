number = input('input number: ')
number_list = list(str(number))
print(number_list)

chs_map = [
    '零', '一', '二', '三', '四', '五', '六', '七', '八', '九'
]
chs_number_list = [chs_map[int(x)] for x in number_list]
print(''.join(chs_number_list))
