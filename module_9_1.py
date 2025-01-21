def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
         results.update({func.__name__: func(int_list)})
    return results

int_list = [12, 4, 75.67, -45, 8.846465849]

def min(int_list):
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result

def max(int_list):
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result

def len_(int_list):
    result = len(int_list)
    return result

def sum(int_list):
    result = 0
    for i in int_list:
        result += i
    return result

def sorted_(int_list):
    result = sorted(int_list)
    return result

def midle(int_list):
    result = 0
    for i in int_list:
        result += i
    result = result / len_(int_list)
    return result


print(apply_all_func(int_list, min, max, sum, midle))
print(apply_all_func(int_list, len_, sorted_))
