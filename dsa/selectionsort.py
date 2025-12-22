def selection_sort(items: list) -> list:
    current_index = 0
    while current_index < len(items):
        min_index = current_index
        
        for i in range(current_index + 1, len(items)):
            if items[i] < items[min_index]:
                min_index = i
                y = current_index
        items[current_index], items[min_index] = items[min_index], items[current_index]
        current_index += 1
        
    return items