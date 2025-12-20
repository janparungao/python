def quick_sort(input_list: list) -> list:
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return input_list
    pivot_value = input_list[0]
    less_list = []
    equal_list = []
    more_list = []
    for element in input_list:

        if element < pivot_value:
            less_list.append(element)
        elif element == pivot_value:
             equal_list.append(element)
        else:
            more_list.append(element)
            
    sorted_less = quick_sort(less_list)
    sorted_more = quick_sort(more_list)
    
    return sorted_less + equal_list + sorted_more
