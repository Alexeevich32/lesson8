from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    str_num = 0
    str_start_byte = file.seek(0)
    for string_ in strings:
        file.write(string_+'\n')
        str_num += 1
        key = (str_num, str_start_byte)
        string_positions[key]= string_
        str_start_byte = file.tell()
    file.close()
    return string_positions

file_name = 'test.txt'
strings = ['Ночь, улица, фонарь, аптека,', 'Бессмысленый и тусклый свет.',
           'Живи, ещё хоть четверть века-', 'Все будет так.Исхода нет.','', 'А.А. Блок']
result = custom_write(file_name, strings)
pprint(result)